callback = """
function getEditorContent() {
    var editor = ace.edit("editor");
    var code = editor.getValue();  // Get the content of the editor

    // Optionally, you could update the content somewhere
    // document.getElementById("codeOutput").textContent = code;
}

function setupEditor() {
    var editor = ace.edit("editor");

    // Enable language tools and features
    ace.config.loadModule('ace/ext/language_tools', function() {
        var langTools = ace.require('ace/ext/language_tools');  // Only require langTools once

        // Set editor options for autocompletion
        editor.setOptions({
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
            enableSnippets: true,
            wrap: true,
            useWrapMode: true,
            showPrintMargin: false,
            tabSize: 4,           // Set the number of spaces for each tab
            useSoftTabs: true,    // Use spaces instead of tabs
            indentedSoftWrap: true // Indent wrapped lines
        });

        // Set the mode to Python for syntax highlighting
        editor.session.setMode("ace/mode/python");
        editor.renderer.setShowGutter(true);
        editor.renderer.setPadding(10);
        editor.$blockScrolling = Infinity;

        // Update the code block on editor change (optional)
        editor.session.on('change', function() {
            getEditorContent();  // Update content whenever editor changes
        });
    });
}

setupEditor();  // Initialize the editor and set it up

"""


dynamics = """
function getEditorContentAutomatic() {
   var editor = ace.edit("editor");
   var code = editor.getValue();
   return code;
}
getEditorContentAutomatic();  // Call the function to get the content
"""
