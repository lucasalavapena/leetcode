defmodule Solution do
  @spec distinct_integers(n :: integer) :: integer
  def distinct_integers(n) do
    max(n-1, 1)
  end
end