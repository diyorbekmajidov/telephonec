(function($) {
    $(document).ready(function() {
        console.log("js ishladi")
        function filterManagement() {
            var statusField = $("#id_status");
            var managementField = $("#id_management");

            if (!statusField.length || !managementField.length) return;

            var statusValue = statusField.val();  // Yangi TextChoices qiymatini olish
            managementField.find("option").hide();

            if (statusValue === "Aparat hodim") {
                managementField.val("");
            } else {
                $.ajax({
                    url: '/check-option-type/',  // Django URL
                    type: 'POST',
                    data: {
                        'status_value': statusValue,  // TextChoices dagi real matn
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    },
                    success: function(response) {
                        if (response.valid) {
                            managementField.empty(); // Tozalash

                            response.data.forEach(function(item) {
                                var option = $("<option></option>").val(item.id).text(item.name);
                                managementField.append(option);
                            });

                            // Agar yangi variantlar bo'lsa, birinchisini tanlash
                            var firstVisible = managementField.find("option:first").val();
                            managementField.val(firstVisible);
                        }
                    }
                });
            }
        }

        // Hodisani bog‘lash
        $("#id_status").change(filterManagement);
        filterManagement(); // Sahifa yuklanganda ishlaydi
    });
})(django.jQuery);
