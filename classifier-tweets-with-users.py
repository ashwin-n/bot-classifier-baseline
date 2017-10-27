#!/usr/bin/python
import random
from  collections import defaultdict
from collections import Counter
import math
import sys
from utils import *

users = getUserData()

def extractTweetFeatures(tokens):
    field_Tweets = readFields('data/metadata/fields-tweet.train')
    field_Users = readFields('data/metadata/fields-users.train')

    phi = defaultdict(float)
    for index, fieldValue in enumerate(tokens):
        sanitizedFieldName = field_Tweets[index].replace('"','')
        if sanitizedFieldName in ['text','favorite_count','reply_count','num_urls','user_id','place']:
        # if index ==1:
            sanitizedFieldValue = fieldValue.strip()
            if sanitizedFieldValue not in ["","NULL","-"]:
                if sanitizedFieldName == 'user_id':
                    user = users[sanitizedFieldValue]
                    # print user
                    for i, v in enumerate(user):
                        sanitizedUserFieldName = field_Users[i].replace('"','')
                        if sanitizedUserFieldName in ['followers_count','friends_count']:
                            sanitizedUserFieldValue = v.strip()
                            uCount = int(sanitizedUserFieldValue)
                            if uCount == 0:
                                phi[sanitizedUserFieldName+': 0'] +=  1
                            else:
                                phi[sanitizedUserFieldName+': !0'] +=  1
                elif sanitizedFieldName in ['favorite_count','reply_count','retweet_count','num_urls']:
                    count = int(fieldValue)
                    if count ==0:
                        phi[sanitizedFieldName+': 0'] +=  1
                    else:
                        phi[sanitizedFieldName+': !0'] +=  1
                elif sanitizedFieldName =='text':
                    tweet = fieldValue.split(" ")
                    for tweetWord in tweet:
                        if len(tweetWord) >2:
                            phi[sanitizedFieldName+':'+tweetWord] +=  1
                    # phi[sanitizedFieldName+':'+fieldValue] +=  1
                else:
                    phi[sanitizedFieldName+':'+fieldValue] +=  1

    return phi

def learnPredictor(trainExamples, featureExtractor, numIters, eta):
    weights = {}
    trainExamples_extracted = []
    print "Extracting features"
    for x, y in trainExamples:
        trainExamples_extracted.append((featureExtractor(x), y))
    print "Done extracting features", len(trainExamples_extracted)
    for t in range(numIters):
        for (phi, y) in trainExamples_extracted:
            if(1 - dotProduct(weights, phi) * y > 0):#max(0, 1-dot(weights, phi))
                increment(weights, eta * y, phi)#Stochastic Gradient Descent ; gradient is -phi*y  , w = w - eta* -phi.y = w+(eta*y).phi
        trainError = evaluatePredictor(trainExamples_extracted, lambda(x) : (1 if dotProduct(x, weights) >= 0 else -1))
        print "Iteration = %d, Train error = %f" %(t , trainError)
    # END_YOUR_CODE
    return weights


trainExamples = readExamples('data/tweets-bots.train','data/tweets-genuine.train')
featureExtractor = extractTweetFeatures
weights = learnPredictor(trainExamples, featureExtractor, numIters=20, eta=0.01)
print "Done training"
outputWeights(weights, 'weights')

testExamples = readExamples('data/tweets-social-bots.test','data/tweets-genuine.test')
testError = evaluatePredictor(testExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
# outputErrorAnalysis(testExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
print "Official: test error = %s" % (testError)