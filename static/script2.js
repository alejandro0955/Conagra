const xValues = ["Feb", "Mar", "Apr", "May", "Jun", "Jul"];

function createGraphs(yValues) {
  for (let i = 0; i < Object.keys(yValues).length; i++) {
    graph = document.createElement("canvas");
    graph.id = "graph" + String(i);
    graph.style.size = 0.5;
    document.getElementById("idkyet").appendChild(graph);

    new Chart("graph" + String(i), {
      type: "line",
      data: {
        labels: xValues,
        datasets: [
          {
            backgroundColor: "#559a42",
            borderColor: yValues[i]["Prediction"] == "Yes" ? "#559a42" : "red",
            fill: false,
            data: [
              yValues[i]["Feb"],
              yValues[i]["Mar"],
              yValues[i]["Apr"],
              yValues[i]["May"],
              yValues[i]["Jun"],
              yValues[i]["Jul"],
            ],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        title: {
          display: true,
          text: yValues[i]["Ingredient"],
          fontSize: 40,
        },
        legend: {
          display: false,
        },
        scales: {
          yAxes: [
            {
              ticks: {
                fontSize: 30,
              },
            },
          ],
          xAxes: [
            {
              ticks: {
                fontSize: 40,
              },
              scaleLabel: {
                display: true,
                labelString: "Predicted to grow: " + yValues[i]["Prediction"],
                fontSize: 40,
                fontColor: yValues[i]["Prediction"] == "Yes" ? "green" : "red",
              },
            },
          ],
        },
      },
    });
  }
}
