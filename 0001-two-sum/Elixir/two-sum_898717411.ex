defmodule Solution do
    @spec two_sum(nums :: [integer], target :: integer) :: [integer]
    def two_sum(nums, target) do
        two_sum_helper(nums, target)
    end
    def two_sum_helper([head|tail], target, position \\ 0, seen \\ %{}) do
        if Map.has_key?(seen, target-head) do
            [Map.get(seen, target-head), position]
        else
            two_sum_helper(tail, target, position + 1, Map.put_new(seen, head, position))
        end
    end
end