from models import Author, Article

def test_create_author(db_session):
    author = Author(firstname='John', lastname='Doe', email='john.doe@example.com')
    db_session.add(author)
    db_session.commit()
    assert author.id is not None

def test_create_article(db_session):
    author = Author(firstname='Jane', lastname='Doe', email='jane.doe@example.com')
    db_session.add(author)
    db_session.commit()
    article = Article(slug='test-article', title='Test Article', content='This is a test article.', author_id=author.id)
    db_session.add(article)
    db_session.commit()
    assert article.id is not None
    assert article.author_id == author.id
