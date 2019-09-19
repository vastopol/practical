module SquareSum where

squareSum :: [Integer] -> Integer

squareSum lst =
    sum $ map (^2) lst
    