let clase = ""
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    clase = serial.readLine()
    if (clase != "") {
        if (clase == "Piedra") {
            basic.showIcon(IconNames.SmallSquare)
        } else if (clase == "Papel") {
            basic.showIcon(IconNames.Square)
        } else if (clase == "Tijera") {
            basic.showIcon(IconNames.Scissors)
        }
    }
})
