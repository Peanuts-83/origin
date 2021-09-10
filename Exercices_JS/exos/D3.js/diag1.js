// Responsive Diag //
// Set of data
var dataset = [31, 64, 42, 28, 16, 32, 64, 10];

// Create our SVG container
var svg = d3.select("#bar-chart")
    .append("svg")
    .attr('viewBox', '-3 0 200 100')
    .attr('preserveAspectRatio', 'xMinYMin');

var bars = svg.append('g')
    .attr('class', 'bars');

// Bind data to chart, and create bars
bars.selectAll('rect')
    .data(dataset)
    .enter()
    .append('rect')
        .attr('x', (d, i) => i * 20 + 15)
        .attr('y', (d) => 100 - d - 20)
        .attr('width', 20)
        .attr('height', (d) => d);

// AXES
const xScale = d3.scaleLinear()
    .domain([0, 8])
    .range([0, 160])

svg.append('g')
    .call(d3.axisBottom(xScale))
    .attr('transform', 'translate(15, 80)');

const yScale = d3.scaleLinear()
    .domain([7, 0])
    .range([0, 70])

svg.append('g')
    .call(d3.axisLeft(yScale).ticks(4))
    .attr('transform', 'translate(15, 10)')

svg.append('g')
    .call(d3.axisRight(yScale).ticks(7))
    .attr('transform', 'translate(175, 10)')


// Mise a l'echelle auto //
// Set of data
/* const data = [31, 64, 42, 28, 16, 32, 64, 10];
// .node().getBoundingClientRect() -> Object containing x/y/width/height/top/right/bottom/left
const width = (d3.select('body').node().getBoundingClientRect()).width;   // == body width
const height = width/2;

// SVG Container
let svg = d3.select('#bar-chart')
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('background', 'lightgrey');

// scaleLinear function to autoScale Diag
const xScale = d3.scaleLinear()
    .domain([0, data.length])
    .range([0, width]);
const yScale = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, height*.9]);

// ADD Bars
svg.append('g')                         // create a group for bars
    .attr('class', 'bars')              // give className for the group
    .selectAll('.bar')                  // selectAll before bars creation!
    .data(data)                         // data binding to upward selection
    .enter()                            // enable to create more bars to fit data
    .append('rect')                     // add bars
        .attr('x', (d,i) => xScale(i))    // posX with index of currentData
        .attr('y', (d) => height - yScale(d))
        .attr('width', xScale(.9))              // width of bar - fixed
        .attr('height', (d) => yScale(d))         // height of bar -  currentData */


// Mise a l'echelle manuelle //
/* // Set of data
const data = [31, 64, 42, 28, 16, 32, 64, 10];
// .node().getBoundingClientRect() -> Object containing x/y/width/height/top/right/bottom/left
const width = (d3.select('body').node().getBoundingClientRect()).width;   // == body width
const height = width/2;

// SVG Container
let svg = d3.select('#bar-chart')
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('background', 'lightgrey');

// ADD Bars
svg.append('g')                         // create a group for bars
    .attr('class', 'bars')              // give className for the group
    .selectAll('.bar')                  // selectAll before bars creation!
    .data(data)                         // data binding to upward selection
    .enter()                            // enable to create more bars to fit data
    .append('rect')                     // add bars
        .attr('x', (d,i) => i*(width/data.length))    // posX with index of currentData
        .attr('y', (d) => height - d*height/100)
        .attr('width', (d,i) => 0.8 * width/data.length)              // width of bar - fixed
        .attr('height', (d) => d * (height/100))         // height of bar -  currentData
 */