(function($) {
    $(document).ready(function() {
        function filterManagement() {
            var statusField = $("#id_status");
            var managementField = $("#id_management");

            if (!statusField.length || !managementField.length) return;

            var statusValue = statusField.val();
            managementField.find("option").hide();

            if (statusValue === "2") {
                managementField.val("");
            } else {
                $.ajax({
                    url: '/check-option-type/',  // Django URL manzili
                    type: 'POST',
                    data: {
                        'status_value': statusValue,
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    },
                    success: function(response) {
                        if (response.valid) {

                            managementField.empty();
                            response.data.forEach(function(item) {
                                var option = $("<option></option>").val(item.id).text(item.name);
                                managementField.append(option);
                            });

                            var firstVisible = managementField.find("option:visible:first").val();
                            managementField.val(firstVisible);
                        }
                    }
                });
            }
        }

        $("#id_status").change(filterManagement);
        filterManagement(); 
    });
})(django.jQuery);
