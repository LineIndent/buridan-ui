from io import StringIO, BytesIO
from random import randint

import requests
import reflex as rx
import pandas as pd


class ChartStruct(rx.Base):
    id: int
    title: str = ""
    xAxis: str = ""
    yAxis: str = ""


class PlotStruct(rx.Base):
    xAxis: str
    yAxis: str
    data: list[dict[str, str]]


class InteractiveChartsState(rx.State):
    # ... Data URL link
    url: str
    # ... Pandas DataFrame variable
    df: pd.DataFrame
    # ... Chart and table variable
    columns: list[str]
    # ... Chart list for iteration
    charts: list[ChartStruct]
    plot: list[PlotStruct]

    async def add_new_chart(self):
        self.charts.append(ChartStruct(id=randint(0, 100000)))

    async def update_chart_axis(self, data: ChartStruct, axis: str, name: str):
        self.charts = [
            (
                ChartStruct(
                    id=item.id,
                    title=item.title,
                    xAxis=name if axis == "x" and item.id == data["id"] else item.xAxis,
                    yAxis=name if axis == "y" and item.id == data["id"] else item.yAxis,
                )
                if item.id == data["id"]
                else item
            )
            for item in self.charts
        ]

    async def compile_chart_data_to_ui(self):
        self.plot = []
        for data in self.charts:
            values = self.df.groupby(data.xAxis)[data.yAxis].sum().reset_index()
            self.plot.append(
                PlotStruct(
                    xAxis=data.xAxis,
                    yAxis=data.yAxis,
                    data=values.to_dict(orient="records"),
                )
            )

    async def get_data_from_url(self):
        self.plot, self.charts = [], []

        try:
            # Make a request to the URL
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses

            # Check the content type
            content_type = response.headers.get("Content-Type")

            if "application/json" in content_type:
                data = response.json()
                self.df = pd.json_normalize(data)  # Normalize JSON data to a DataFrame
            elif "text/csv" in content_type or self.url.endswith(".csv"):
                self.df = pd.read_csv(StringIO(response.text))
            elif (
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                in content_type
            ):
                self.df = pd.read_excel(BytesIO(response.content))
            else:
                raise ValueError(
                    "Unsupported content type. Please provide a URL with JSON or CSV data."
                )

            self.columns = self.df.columns.to_list()

        except Exception as e:
            self.df = pd.DataFrame()
            self.columns = []
            return rx.toast.error(f"An error occurred: {e}")
