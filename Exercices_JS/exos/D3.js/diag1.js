// Set of data
const data = [31, 64, 42, 28, 16, 32, 64, 10];

// SVG Container
let svg = d3.select('#bar-chart')
    .append('svg')
    .attr('width', 200)
    .attr('height', 100)
    .style('background', 'lightgrey');

// ADD Bars
svg.append('g')                         // create a group for bars
    .attr('class', 'bars')              // give className for the group
    .selectAll('.bar')                  // selectAll before bars creation!
    .data(data)                         // data binding to upward selection
    .enter()                            // enable to create more bars to fit data
    .append('rect')                     // add bars
        .attr('x', (d,i) => i*25 +3)    // posX with index of currentData
        .attr('y', 0)
        .attr('width', 20)              // width of bar - fixed
        .attr('height', d => d)         // height of bar -  currentData
        .attr('y', d => 100-d)          // miroring on Y axis
