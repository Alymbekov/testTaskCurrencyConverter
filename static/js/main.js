$(function () {
    const host = 'api.frankfurter.app';
    fetch(`https://${host}/currencies`)
      .then(resp => resp.json())
      .then((data) => {
          fetchCurencies(data)
      });

    $('.converter-form').submit(fetchConverterResponse)
})


function fetchConverterResponse(e) {
    e.preventDefault()

    let form = $(this);
    let url = form.attr('action');

    if($('.in_data').val() === '')$('.in_data').attr('disabled',true);
    if($('.out_data').val() === '')$('.out_data').attr('disabled',true);
    $('.table-body').html('')

    $.ajax({
        type: 'GET',
        url,
        data: form.serialize(),
        success: function (data) {
            console.log(data)
            $('.select-currency').removeAttr('disabled');
            $('.table-body').append(`
                <tr>
                    <td>${data.base}</td>
                    <td>${data.amount}</td>
                </tr>   
            `);

            $('.table-date').text(data.date.replace(/\-/gi,'/'))

            for (key in data.rates){
                $('.table-body').append(`
                    <tr>
                        <td>${key}</td>
                        <td>${data.rates[key]}</td>
                    </tr>
                `);
            }

        }
    })


}

function fetchCurencies(data) {
    for (key in data){
        // let $newOption = $(`
        //     <option value="${key}">${key} - ${data[key]}</option>
        // `)
        // $('.in_data').append($newOption)
        // $('.out_data').append($newOption)
        $('.select-currency').append(`
            <option value="${key}">${key} - ${data[key]}</option>
        `)
    }
}