"""
    File: bball.py
    Author: Anna Rowena Waldron
    Purpose: Program that analyzes historical win-loss data for basketball
        and computes the win ratio for each team and it's conference.
    Course/semester/Sect: CSC 120, spring18, 1G
"""

def main():
    """ Main function calling function initial and catching the return value
    as a list, and calling the create function passing the returned value
    as a parameter.
    """
    Flist = initial()
    create(Flist)
    
def initial():
    """ Function that uses user input to read in a file and structure the
    data into a list of lists.Data is cleaned up and names are grouped
    together. Uses nested for loops to group names of teams in one index
    of a list and groups the words in the name of the conference together
    at the following index.
    Parameters: N/A
    Returns: all data as strings for each team in one line lists.
    Pre-COndition: N/A
    Post-Condition: Flist is a list of lists containing all data for the
        rest of the programs computations.
    """
    file = open(input())
    Flist = []
    for line in file:
        p = line.split()
        inner = []
        assert len(inner) <= 4
        if p[0][0] == '#':
            continue
        for i in range(len(p)):
            ### INVARIANT: concatenate conference names in parenthesis 
            if p[i][0] == '(' and p[i][-1] != ')':
                p[i] += ' ' + p[i + 1]
                p[i] = p[i][1:-1]
            elif p[i][0] == '(' and p[i][-1] == ')':
                p[i] = p[i][1:-1]
            elif (p[i][0] != '(' and p[i][-1] == ')'):
                continue
            inner.append(p[i])
        z = inner[:-3]
        hold = ''
        for i in range(len(z)):
            ### ASSUMPTION: hold is the entire name of the team 
            hold += z[i] + ' '
        inner.reverse()
        b = inner[:3]
        b.append(hold)
        b.reverse()
        Flist.append(b)
    return Flist

def create(Flist):
    """Function which access the classes using the data list to use
    the methods in the classes to the print out the results.
    Parameters: Flist contains all data of teams and conferences.
    Returns: N/A prints out results
    Pre-Condition: Flist is a list of list of strings.
    Post-Condition: N/A"""
    b = ConferenceSet()
    for q in range(len(Flist)):
        ### INVARIANT: b set increases by one or none new conference(s).
        conp = Conference(Flist[q][-3])
        for i in range(len(Flist)):
            assert type(Flist) == list
            newT = Team(Flist[i])
            if newT.conf() == conp.name():
                conp.add(newT)
            
        b.add(conp)
    for j in b.best():
        print(j)
    
class ConferenceSet:
    """Class of conferences grouped together. """
    def __init__(self):
        """Initializes COnferenceSet onject with a list. """
        self._set = []
                   
    def add(self, con):
        """Appends conference objects to the list.
        Pre-Con: con is a conference object"""
        assert type(con) == Conference 
        for i in range(len(self._set)):
            if con.name() == self._set[i].name():
                return
        self._set.append(con)
            
    def best(self):
        """Finds the largest value of win ratios among all the conferences
        and appends the conferences with this value to the list best_conf.
        Post-Con: best_conf is a list of conference objects of the top
            win average."""
        maxi = 0
        prior = 0
        best_conf = []
        for wins in self._set:
            assert type(prior) == float or int
            prior = wins.win_ratio_avg()
            maxi = max(prior, maxi)
        for winny in self._set:
            assert maxi >= winny.win_ratio_avg()
            if winny.win_ratio_avg() == maxi:
                best_conf.append(winny)
        return best_conf
            
class Conference:
    """Class of a Conference with its teams for those conferences in its list.
    Groups conference with its teams."""
    def __init__(self, conf):
        """Conf is the name of the conference as a string. Creates a list
        to store teams in the conference."""
        assert type(conf) == str
        self._name = conf
        self._listing = []
        
    def __contains__(self, team):
        """" Checks if the team object is in the list of teams. Parameter team
        is a Team class object. """
        assert type(team) == Team
        return team in self._listing
    def name(self):
        """Returns name of the conference. """
        return self._name
    def add(self, team):
        """ Appends Team object to the list of teams. team is a Team class
        object."""
        assert type(team) == Team
        self._listing.append(team)
        
    def win_ratio_avg(self):
        """Computes the win ratio average of all teams in that conference and
        returns that value."""
        wins = 0
        games = 0
        for t in self._listing:
            ### INVARIANT: after for loop games != 0.
            wins += float(t.win_ratio())
            games += 1
        if games != 0: 
            return (wins / games)

    def __str__(self):
        """Makes the print and string method of this class. Returns the
        formatting of the object with its conference name and average win
        ratio."""
        return "{} : {}".format(self._name, str(self.win_ratio_avg()))  
    
class Team:
    """Class of basketball team and its conference name and win ratio. """
    def __init__(self, line):
        """Sets attributes for object, name of the team, name of the conference
        and the win ratio of wins over total games.
        Pre-Con: line is a list of strings of data for the team."""
        assert type(line) == list
        self._name = line[0]
        self._conf = line[1]
        self._win_ratio = str(int(line[-2]) / (int(line[-2]) + int(line[-1])))

    def name(self):
        """Returns the name of the team. """
        return self._name
    def conf(self):
        """Returns name of the teams conference. """
        return self._conf
    def win_ratio(self):
        """Returns win ratio of the team. """
        return self._win_ratio

    def __str__(self):
        """Returns the string operation for the class in the format of
        the team name and win ratio."""
        return "{} : {}".format(self._name, self._win_ratio)

"""Calls main function. """
main()
