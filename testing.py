import numericOperation as nm

def test_multi():
  assert nm.multiply_op(10,11) == 110
  
def test_sub():
  assert nm.sub_op(11,10) == 1
  
def test_add():
  assert nm.add_op(11,10) == 21

def test_pow():
  assert nm.pow_op(2,2) == 4
