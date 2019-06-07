process.stdin.resume();
process.stdin.setEncoding('ascii');

let inputStdin = "";
let inputStdinArray = "";
let linesCounter = 0;

process.stdin.on('data', function (data) {
    inputStdin += data;
});

process.stdin.on('end', function () {
    inputStdinArray = inputStdin.split("\n");
    processInputData();
});

const calculateArea = (shape, values) => {
    const allowedShapes = ['square', 'rectangle', 'circle', 'triangle']

    return new Promise((resolve, reject) => {
        const shapeName = shape.toLowerCase();
        const shapeIsValid = allowedShapes.indexOf(shapeName);
        const result = 0

        if (shapeIsValid === -1) {
            return reject(-1);
        }

        if (shapeName === 'square') {
            result = values[0] * values[0];
            resolve(result);
        }
    })

}

let getAreas = (shapes, sizesForEachShape) => {
    const areasToCalculate = []
    for (var shape = 0; shape < shapes.length; shape++) {
        const shapeName = shapes[shape].trim();
        let shapeSizes = sizesForEachShape[shape];
        shapeSizes = shapeSizes.trim().split(',')
        areasToCalculate.push(calculateArea(shapeName, shapeSizes));
    }
    const testPromise = areasToCalculate[0].then(result => console.log('result for ', shapes[0], ' was ', result));
}

const processInputData = () => {
    const shapes = []
    const shapeSizes = []
    const inputLength = inputStdinArray.length;

    // for (let input = 1; input < inputLength; input++) {
    //     inputLine = inputStdinArray[input];
    //     lineValue = inputLine.split(',')

    //     if (!Number(lineValue[0])) {
    //         if (lineValue[0].length) {
    //             shapes.push(inputLine);
    //         }
    //     } else {
    //         shapeSizes.push(inputLine);
    //     }
    // }
    shapes = ['square', 'trapezium', 'triangle']
    shapeSizes = ['2', '3,3,4', '1,3']
    const result = getAreas(shapes, shapeSizes);

}