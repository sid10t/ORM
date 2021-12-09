# Software Architecture and Design Patterns -- Lab 3 starter code
# An implementation of the Service Layer
# Copyright (C) 2021 Hui Lan


# word and its difficulty level
WORD_DIFFICULTY_LEVEL = {'starbucks':5, 'luckin':4, 'secondcup':4, 'costa':3, 'timhortons':3, 'frappuccino':6}

import pytest
class UnknownUser(Exception):
    pass

class NoArticleMatched(Exception):
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    '''
    pass
    # try:
    #     pass
    # except Exception:
    #     print("No articles, sorry!")
    #     raise
    # # raise Exception("Don't find this article, sorry!")


def read(user, user_repo, article_repo, session):
    u = user_repo.get(user.username)
    if u == None or u.password != user.password:
        #with pytest.raises(Exception):
        raise UnknownUser()

    articles = article_repo.list()
    if articles == None:
        #with pytest.raises(Exception):
        raise NoArticleMatched()

    words = session.execute(
        'SELECT word FROM newwords WHERE username=:username',
        dict(username=user.username),
    )

    sum = 0
    count = 0
    for word in words:
        sum += WORD_DIFFICULTY_LEVEL[word[0]]
        count += 1
    
    if count == 0:
        count = 1

    average = round(sum / count) + 1
    if average < 3:
        average = 3
    
    for article in articles:
        if average == article.level:
            return article.article_id

    return average


