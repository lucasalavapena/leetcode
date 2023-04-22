defmodule Solution do
    @spec difference_of_sum(nums :: [integer]) :: integer
    def difference_of_sum(nums) do
        abs((Enum.map(nums, fn x -> element_sum(x) end) |> Enum.sum) - Enum.sum(nums))
    end
    def element_sum(x) do
        Integer.to_string(x) |>
        String.split("", trim: true) |>
        Enum.map(fn y -> String.to_integer(y) end) |>
        Enum.sum
    end
end