# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec max_depth(root :: TreeNode.t | nil) :: integer
  def max_depth(root) do
    case root do
        nil -> 0
        node -> 1 + max(max_depth(root.left), max_depth(root.right))
    end
  end
end