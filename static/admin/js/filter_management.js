(function($) {
    $(document).ready(function() {
        function filterManagement() {
            var statusField = $("#id_status");
            var managementField = $("#id_management").closest('.form-row');

            if (!statusField.length || !managementField.length) return;

            var statusValue = statusField.val();

            if (statusValue === "Aparat hodim") {
                managementField.hide();  // 🔴 Yashirish
                $("#id_management").val("");  // 🔴 Maydonni bo‘sh qilish
            } else {
                managementField.show();  // 🟢 Ko‘rsatish
                
                $.ajax({
                    url: '/check-option-type/',
                    type: 'POST',
                    data: {
                        'status_value': statusValue,
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    },
                    success: function(response) {
                        if (response.valid) {
                            var managementSelect = $("#id_management");
                            managementSelect.empty();
                            
                            response.data.forEach(function(item) {
                                var option = $("<option></option>").val(item.id).text(item.name);
                                managementSelect.append(option);
                            });

                            var firstVisible = managementSelect.find("option:visible:first").val();
                            managementSelect.val(firstVisible);
                        }
                    }
                });
            }
        }

        $("#id_status").change(filterManagement);
        filterManagement();
    });
})(django.jQuery);
