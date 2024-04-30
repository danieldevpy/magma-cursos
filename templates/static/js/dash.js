  
var ctx;
var data_json;


function LoadChart(){
    const _labels = []
    const _values = []

    for (var key in data_json) {
        if (data_json.hasOwnProperty(key)) {
            var value = data_json[key];
            _labels.push(key);
            _values.push(value);

        }
    }
    new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: _labels,
          datasets: [{
            label: 'quantidade',
            data: _values,
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    
}



window.addEventListener("load", function(event){
    ctx = document.getElementById('myChart');
    data_str = document.getElementById("json").innerText;
    console.log(data_str);
    data_json = JSON.parse(data_str.replace(/'/g, '"'));
    console.log(data_json);
    LoadChart();
});