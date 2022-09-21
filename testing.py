import numericOperation

def test_multi():
  assert muliply_op(10,11) == 110
  
def test_sub():
  assert sub_op(11,10) == 1
  
def test_add():
  assert add_op(11,10) == 21

def test_pow():
  assert pow_op(2,2) == 4
