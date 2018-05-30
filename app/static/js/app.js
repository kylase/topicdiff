(function (d3) {
    'use strict';
    $("#topicdiff").submit(function (event) {
        if ($(".viz").children().length) {
            $(".viz").empty();
        }

        var data = {
            'content': [],
            'model': 'wikipedia',
            'threshold': 0.01
        };

        $("textarea[name=content]").each(function () {
            data.content.push($(this).val());
        });

        if (!data.content.filter(content => content !== "").length) {
            delete data.content
        }

        var content = {
            width: $("#topicdiff").width(),
            height: 300
        };

        var svg = d3.select(".viz").append("svg")
                    .attr("width", content.width)
                    .attr("height", content.height);

        d3.json('/api/documents/compare', {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
            }
        }).catch((err) => {
            console.log(err);
        }).then((response) => {
            $(".viz").prepend(
                '<h3>Topic Cloud <small class="text-muted"> based on model trained using <mark>' + response.model.name + '</mark> with <mark>' + response.model.total_topics + '</mark> topics that have at least <mark>' + response.model.threshold * 100 + '%</mark> association</small></h3>' +
                '<p>Topics with <span class="both">purple</span> shade means they are common to both documents. ' +
                'Topics with <span class="left">red</span> and <span class="right">blue</span> shade means they are exclusive to each respective document (denoted by the colour of the border of the text boxes).</p>'
            );

            let margin = {top: 40, right: 30, bottom: 40, left: 30},
                number_per_row = 20,
                box_size = (content.height - (margin.top + margin.bottom)) / (response.model.total_topics / number_per_row);

            let topics_groups = svg.selectAll("g")
                                    .data(Object.entries(response["data"]))
                                    .enter()
                                    .append("g");

            let labels = topics_groups.append("text")
                .attr("class", "topic-label")
                .attr("x", d => {
                    let canvas_width = content.width - (margin.left + margin.right);
                    return ((parseInt(d[0]) + 1) / number_per_row - Math.floor(parseInt(d[0]) / number_per_row)) * canvas_width
                })
                .attr("y", d => {
                    let canvas_height = content.height - (margin.top + margin.bottom);
                    return Math.floor(parseInt(d[0]) / number_per_row) * canvas_height / (response.model.total_topics / number_per_row) + margin.top
                })
                .text(d => {
                    return d[0]
                });

            topics_groups.insert("rect", ":first-child")
                .attr("class", d => {
                    const sum = (a, b) => a + b + 2;
                    const idx = Object.keys(d[1]).map(Number).reduce(sum);
                    switch (idx) {
                        case 0:
                            return "topic-label-box " + "left"
                            break;
                        case 1:
                            return "topic-label-box " + "right"
                            break;
                        case 3:
                            return "topic-label-box " + "both"
                            break;
                    }
                })
                .attr("x", function (d) {
                    const x = d3.select(this.parentNode).select(".topic-label").node().getBBox().x;
                    const width = d3.select(this.parentNode).select(".topic-label").node().getBBox().width;

                    return x + width / 2 - box_size / 2
                })
                .attr("y", function (d) {
                    const y = d3.select(this.parentNode).select(".topic-label").node().getBBox().y;
                    const height = d3.select(this.parentNode).select(".topic-label").node().getBBox().height;
                    return y + height / 2 - box_size / 2
                })
                .attr("width", box_size)
                .attr("height", box_size);

            $("button").text("Re-submit");
        })
        event.preventDefault();
    })
})(window.d3)