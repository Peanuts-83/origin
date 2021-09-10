// DIAGRAM //
const datas = [15, 36, 18, 29, 23, 38,
    12, 30, 11];

d3.select('body')
    .insert('svg', 'script')
    .classed('row', true)
    .classed('svg', true)
    .attr('height', '250')
    .attr('width', '450');

d3.select('body').insert('h1', 'svg').text('D3.js tests').style('margin', '10px').style('align-self', 'flex-start').style('color', 'darkblue');

d3.select('.svg')
    .selectAll('rect')
    .data(datas)
    .enter()
    .append('rect')
    .attr('x', 70)
    .attr('y', function (d, i) {
        return i * 20;
    })
    .attr('width', function (d, i) {
        return d * 10;
    })
    .attr('height', 15)
    .classed('barre', true)
    /* .on('mouseover', function(){
        d3.select(this).classed('hidden', false);
    }) */
    /*  */;



const legendes = ['0-10 ans', '10-20 ans', '20-30 ans', '30-40 ans', '40-50 ans', '50-60 ans', '60-70 ans', '70-80 ans', '80-90 ans'];

d3.select('.svg')
    .selectAll('text')
    .data(legendes)
    .enter()
    .append('text')
    .text((d) => d)
    .classed('text', true)
    .attr('y', function (d, i) {
        return i * 20 + 12;
    })
    .attr('x', 0);

d3.select('.svg')
    .selectAll('texts')
    .data(datas)
    .enter()
    .append('text')
    .text(function (d) {
        return d + ' %';
    })
    .classed('text', true)
    .attr('y', function (d, i) {
        return i * 20 + 12;
    })
    .attr('x', function (d, i) {
        return (d + 3) * 10;
    });




// PIE //
// Values of data
const camDatas = { a: 9, b: 20, c: 30, d: 8, e: 12 }

// Dimensions of the graph
const width = 450,
    height = 450,
    margin = 40;

// RADIUS of the pieplot is half width or height
const radius = Math.min(width, height) / 2 - margin;

// CREATE Div and place svg, then build 'g' node
const svg = d3.select('body')
    .insert('div', 'script')
    .classed('camembert', true)
    .classed('row', true)
    .append('svg')
    .attr('height', height)
    .attr('width', width)
    .append('g')
    .attr('transform', `translate(${width / 2}, ${height / 2})`);   // position gNode in the middle of svg

// SET color scale // schemSet2 is one set of colors, others are available
const color = d3.scaleOrdinal().range(d3.schemeSet2);

// Compute position of eachgroup on the pie
const pie = d3.pie().value(function (d) { return d[1] })
const data_ready = pie(Object.entries(camDatas));   // Group 1 goes from 0 deg to x deg...

// SHAPE helper for arcs
const arcGenerator = d3.arc()
    .innerRadius(0)
    .outerRadius(radius);

// BUILD pie chart. Each part built using the arc function
svg.selectAll('mySlices')
    .data(data_ready)
    .join('path')
    .attr('d', arcGenerator)
    .attr('fill', function (d) { return (color(d.data[0])) })
    .attr('stroke', 'black')
    .style('stroke-width', '2px')
    .style('opacity', .7);

// BUILD Anotations
svg.selectAll('mySlices')
    .data(data_ready)
    .join('text')
    .text((d) => 'grp ' + d.data[0])
    .attr('transform', function (d) { return (`translate(${arcGenerator.centroid(d)})`) })
    .style('text-anchor', 'middle')
    .style('font-size', 17);




// BUBBLE CHART //
// set the dimensions and margins of the graph
const margin3 = { top: 10, right: 20, bottom: 30, left: 50 },
    width3 = 500 - margin3.left - margin3.right,
    height3 = 420 - margin3.top - margin3.bottom;

// append the svg object to the body of the page
const svg3 = d3.select('body').insert("svg", "script")
    .attr('id', '#my_dataviz')
    .attr("width", width3 + margin3.left + margin3.right)
    .attr("height", height3 + margin3.top + margin3.bottom)
    .append("g")
    .attr("transform", `translate(${margin3.left},${margin3.top})`);

//Read the data
d3.csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/4_ThreeNum.csv").then(function (data) {

    // Add X axis
    const x = d3.scaleLinear()
        .domain([0, 10000])
        .range([0, width3]);
    svg3.append("g")
        .attr("transform", `translate(0, ${height3})`)
        .call(d3.axisBottom(x));

    // Add Y axis
    const y = d3.scaleLinear()
        .domain([35, 90])
        .range([height3, 0]);
    svg3.append("g")
        .call(d3.axisLeft(y));

    // Add a scale for bubble size
    const z = d3.scaleLinear()
        .domain([200000, 1310000000])
        .range([1, 40]);

    // -1- Create a tooltip div that is hidden by default:
    var tooltip = d3.select("#my_dataviz")
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "black")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("color", "white")

    // -2- Create 3 functions to show / update (when mouse move but stay on same circle) / hide the tooltip
    var showTooltip = function (d) {
        tooltip
            .transition()
            .duration(200)
        tooltip
            .style("opacity", 1)
            .html("Country: " + d.country)
            .style("left", (d3.mouse(this)[0] + 30) + "px")
            .style("top", (d3.mouse(this)[1] + 30) + "px")
    }
    var moveTooltip = function (d) {
        tooltip
            .style("left", (d3.mouse(this)[0] + 30) + "px")
            .style("top", (d3.mouse(this)[1] + 30) + "px")
    }
    var hideTooltip = function (d) {
        tooltip
            .transition()
            .duration(200)
            .style("opacity", 0)
    }

    // Add dots
    svg3.append('g')
        .selectAll("dot")
        .data(data)
        .join("circle")
        .attr("cx", d => x(d.gdpPercap))
        .attr("cy", d => y(d.lifeExp))
        .attr("r", d => z(d.pop))
        .style("fill", "#69b3a2")
        .style("opacity", "0.7")
        .attr("stroke", "black")

})