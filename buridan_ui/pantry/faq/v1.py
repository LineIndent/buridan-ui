import reflex as rx

data: list[dict[str, str]] = [
    {
        "question": "Can I cancel at anytime?",
        "answers": "Yes, you can cancel anytime no questions are asked while you cancel but we would highly appreciate if you will give us some feedback.",
    },
    {
        "question": "My team has credits. How do we use them?",
        "answers": "Once your team signs up for a subscription plan. This is where we sit down, grab a cup of coffee and dial in the details.",
    },
    {
        "question": "How does Buridan's UI pricing work?",
        "answers": "Our subscriptions are tiered. Understanding the task at hand and ironing out the wrinkles is key.",
    },
    {
        "question": "How secure is Buridan/Ui?",
        "answers": "Protecting the data you trust is our first priority. This part is really crucial in keeping the project in line to completion.",
    },
    {
        "question": "How do I get access to a theme I purchased?",
        "answers": "If you lose the link for a theme you purchased, don't panic! We've got you covered. You can login to your account, tap your avatar in the upper right corner, and tap Purchases. If you didn't create a login or can't remember the information, you can use our handy Redownload page, just remember to use the same email you originally made your purchases with.",
    },
    {
        "question": "Upgrade License Type",
        "answers": "There may be times when you need to upgrade your license from the original type you purchased and we have a solution that ensures you can apply your original purchase cost to the new license purchase.",
    },
]


def question_and_answer(question: str, answer: str):
    return rx.hstack(
        rx.vstack(
            rx.box(rx.icon(tag="circle-help", size=15), padding="5px 0px"),
            align="start",
            height="100%",
        ),
        rx.vstack(
            rx.text(question, weight="bold", color=rx.color("gray", 11)),
            rx.text(answer, weight="medium", color=rx.color("gray", 12)),
            align="start",
        ),
        width="100%",
        align="start",
        padding="16px 0px",
        border_top=f"1px solid {rx.color('slate', 11)}",
    )


def faq_v1():
    return rx.vstack(
        rx.heading(
            "Frequently Asked Questions",
            size="5",
            weight="bold",
            align="center",
        ),
        *list(
            map(
                lambda item: question_and_answer(item["question"], item["answers"]),
                data,
            )
        ),
        width="100%",
        max_width="35em",
        height="100%",
    )
