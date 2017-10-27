# Bot Classifier Baseline:

Quick and simple Binary Classifier to determine if the tweets are from a Bot or Human, to serve as baseline for CS 221 Project.

Linear Classifier that uses the following features:

##### Tweet:
- Text
- No. of favorites
- No. of replies
- No. of URLs
- Location 
##### User:
- No. of Followers
- No. of Friends.

### Results on Test Data
**Sample Size:**
Training Data : ~50K tweets
Test Data : ~140K tweets

| Category | Success Rate |
| ------ | ------ |
| True Positive | 21.21% |
| False Positive | 26.07% |
| True Negative | 31.17% |
| False Negative | 21.53% |

**Total Error Rate : 47.6%**

### Running the code


```sh
$ python classifier-tweets-with-users.py
```

### Data Courtesy:
https://botometer.iuni.iu.edu/bot-repository/datasets.html

### Contributors:
 - Ananth Rao
 - Ashwin Neerabail
- Yatharth Agarwal