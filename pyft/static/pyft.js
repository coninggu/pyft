$(document).ready(function () {
    var editor = ace.edit("code");
    editor.getSession().setMode("ace/mode/python");
    editor.getSession().setUseSoftTabs(true);
    editor.getSession().setUseWrapMode(true);
    editor.setShowPrintMargin(false);
    editor.setAutoScrollEditorIntoView(true);
    editor.setOption("minLines", 30);
    editor.setOption("maxLines", Infinity);

    $("#format").on("click", function (e) {
        var data = {
            code: editor.getValue(),
            style: $(":radio[name=code_style]:checked").val(),
        }

        if (!data['code']) {
            return false;
        }

        $.ajax({
            type: 'POST',
            url: "/convert",
            async: false,
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data),
            dataType: 'json',
            success: function (result) {
                result = JSON.parse(result)
                if (result.status == 'ok') {
                    $("#error_alert").addClass('hide');
                    editor.getSession().setValue(result.result.reformatted_code)
                }
                else if (result.status == 'error') {
                    $("#error_alert").removeClass('hide');
                    $("#error_msg").text(result.message);
                }
            },
        });
    });

    $("#clear").on("click", function (e) {
        editor.setValue();
    })
})
