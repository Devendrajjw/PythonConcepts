from demoExamples.demo4.sample import add


def test_add(sample_data):
    mydata=sample_data(3,5)
    result= add(mydata["a"],mydata["b"])
    assert result==8


