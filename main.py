#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycol = mydb['names']


# flag = 1

def UserOpinion(pos, neg, _id):

    userOpinion = input('Do you think this output is correct by choosing Y OR N:')

    if userOpinion == 'y' or userOpinion == 'Y':

        myquery = {'_id': _id}
        newvalues = {'$set': {'PostiveCount': pos + 1}}

        mycol.update_one(myquery, newvalues)
    elif userOpinion == 'n' or userOpinion == 'N':

        myquery = {'_id': _id}
        newvalues = {'$set': {'NegativeCount': neg + 1}}

        mycol.update_one(myquery, newvalues)


def genderFinder():

    value = input('Enter your Name: ')
    name = value.casefold()

    x = mycol.find_one({'name': name})

    if x is not None:

        pos = x['PostiveCount']
        neg = x['NegativeCount']

        print ("NegativeCount",neg,"PositiveCount",pos)

        if neg == 0 and pos == 0 or pos == neg:


            if name[-1] == 'a':
                print (value + ' is a girl')

                UserOpinion(pos, neg, x['_id'])
            else:

                print (value + ' is a boy')
                UserOpinion(pos, neg, x['_id'])

        elif pos > neg :

            if name[-1] == 'a':
                print (value + ' is a girl')
                UserOpinion(pos, neg, x['_id'])

            else:

                print (value + ' is a boy')
                UserOpinion(pos, neg, x['_id'])    

        else :
            
            if name[-1] == 'a':
                    print (value + ' is a boy')

                    UserOpinion(pos, neg, x['_id'])

            else:
                    print (value + ' is a girl')

                    UserOpinion(neg, pos, x['_id'])    



            





    else:

        temp = mycol.insert_one({'name': name, 'PostiveCount': 0,
                                'NegativeCount': 0})

        if name[-1] == 'a':
            print (value + ' is a girl')

            UserOpinion(0, 0, temp.inserted_id)
        else:

            print (value + ' is a boy')
            UserOpinion(0, 0, temp.inserted_id)


genderFinder()


