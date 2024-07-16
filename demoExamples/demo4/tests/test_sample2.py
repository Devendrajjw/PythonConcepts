from demoExamples.demo4.sample import multiply

def test_multiply(sample_data):
    mydata=sample_data(3,5)
    result= multiply(mydata["a"],mydata["b"])
    assert result==15
