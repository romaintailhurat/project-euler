import Text.Printf
import Numeric

-- Data
oneToTen = [1..10]

oneToHundred = [1..100]

-- Functions

square x = x ** 2

squares list = map square list

sumList list = sum list

-- Utils

printLargeNumber n = putStrLn $ Numeric.showFFloat Nothing n ""

-- Run

sumOfSquares = sum (squares oneToHundred)

squareOfSum = square (sum oneToHundred)

diff = squareOfSum - sumOfSquares



main = printLargeNumber diff
