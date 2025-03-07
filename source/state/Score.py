class Score:
    '''
    This class is used to keep track of the score of the player.
    '''
    def __init__(self, max_score=0):
        self.score = 0
        self.max_score = max_score
        
    def add_points(self, points):
        '''
        Add points to the score.
        '''
        self.score += points

    def subtract_points(self, points):
        '''
        Subtract points from the score.
        '''
        self.score -= points
        self.score = max(0, self.score)

    def reset(self):
        '''
        Reset the score to 0 when game ends.
        '''
        self.score = 0

    def get_score(self):
        '''
        Get the current score.
        '''
        return self.score