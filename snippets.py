#### Python

list_str_set = [1,2,3]
for i, v in enumerate(list_or_str):
    print(i, v)

all_chars = ['a', 'd', 'e']
char_indices = {c:i for i, c in enumerate(all_chars)}
char_dict = {i:c for i, c in enumerate(all_chars)}

#### Regular Expression
# TODO...
# ref to: Quora/Quora-Feature-Enginnering.ipynb
import re

pattern1 = re.compile(r'(?<=\w)([\?\.,\)])')
pattern2 = re.compile(r'([\(])(?=\w)')

def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    return title_search.group(1) if title_search else "_NO_TITLE_"

#### numpy

import numpy as np
image = np.zeros((256, 256, 3), dtype=np.float32)

#### Pandas

import pandas as pd
from pandas import Series, DataFrame

dtype = {
    'id': np.int8,
    'qid1': np.int8,
    'qid2': np.int8,
    'question1': np.str,
    'question2': np.str,
    'is_duplicate': np.int8
}
train = pd.read_csv('train.csv', dtype=dtype)
train = pd.read_csv('train.csv', encoding='gbk')
train = pd.read_csv('file.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

Series(np.arange(3, 6), index=['a','b','c'], dtype=np.int32)

X_all = DataFrame({
    'cover_ratio': [1,2,3],
    'occur_ratio': ['a', 'b', 'c']
})
DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

train.loc[[6, 5, 3], ['MasVnrType', 'MasVnrArea', 'Electrical']]

all_titles = pd.concat([train.title, test.title]).unique()

df.sort_values(by='ratio', ascending=False, inplace=True)
seris.sort_values(ascending=False)

train.drop(['f1', 'f2'], axis=1, inplace=True)
train.drop(train[train.score > 800].index, inplace=True)
train.drop(train[(train.score > 400) & (train.target == 1)].index, inplace=True)

num_features = train.select_dtypes(exclude = ['object']).columns
cat_features = train.select_dtypes(include = ["object"]).columns

def start_with(q, symbols):
    s = q.split()
    return int(s[0] in symbols) if len(s) > 0 else 0

train['q1_start_with_what'] = train['question1_refine'].apply(start_with, symbols=('what', "what's"))

df = df1.merge(df2, how='left', left_on='Idx', right_on='Idx')

#### Feature Engineering

def fill_nan(f, method):
    if method == 'most':
        common_value = pd.value_counts(train_master[f], ascending=False).index[0]
    elif method == 'mean:
        common_value = train_master[f].mean()
    train_master.loc[train_master[f].isnull(), f] = common_value
# 通过pd.value_counts(train_master[f])的观察得到经验
fill_nan('UserInfo_1', 'most')


submission = pd.DataFrame({
    "id": test.id,
    "result": y_pred
})
submission.to_csv('prediction.csv', index=False)

ndarray.to_csv('prediction.csv', header=True, index=True)

#### matplotlib
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
%matplotlib inline

# Figure
fig =plt.figure(num=1, figsize = (10, 10))

# Axes，单个axes
ax = fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes', ylabel='Y-Axis', xlabel='X-Axis')
plt.show()

# 绘图
# 这样把个的东西绘制在一个图上！
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)#绘制线
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')#绘制散点图

为了简便，也有plt.plot，plt.title，plt.scatter，plt.xlim，plt.show。不过这是快捷用法。

# 多个Axes
fig, axes = plt.subplots(2, 2, figsize = (10, 10), sharex=True)
axes[0,0].set(...title,xlim...)
axes[0,0].imshow(…)
axes[0,0].plot(…)
axes[0,0].scatter(…)
for ax in axes.flat:
    ax.plot(…)
plt.show()

subplots直接返回fig和axes，是fig = plt.figure()，ax = fig.add_subplot(111)等等的简单写法。。

# 3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def scatter_3d(data):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.scatter(data[0], data[1], data[2], c='r', marker='o')

#### Seaborn

import seaborn as sns
sns.set(style='whitegrid')

sns.stripplot(data=train.SalePrice, jitter=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5))
sns.distplot(train.SalePrice, fit=norm, ax=ax1)
sns.distplot(np.log1p(train.SalePrice), fit=norm, ax=ax2)

# advanced
num_melt = pd.melt(train, id_vars=['SalePrice'], value_vars = [f for f in numerical_features])
g = sns.FacetGrid(data=num_melt, col="variable", col_wrap=4, sharex=False, sharey=False)
g.map(sns.regplot, 'value', 'SalePrice')
g.map(sns.distplot, "value")
g.map(sns.countplot, 'value', palette="muted")
g.map(sns.boxplot, 'value', 'SalePrice', palette="muted")
g.map(sns.stripplot, 'value', 'SalePrice', jitter=True, palette="muted")

corr = train.corr()
fig, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(corr, cmap=sns.diverging_palette(240, 10, as_cmap = True), ax=ax)

#### Random
# TODO...
from random import randint

np.random.uniform() < EPSILON
np.random.choice([1,2,3])

#### cv2 opencv
# pip install opencv-python
import cv2
img = cv2.imread(path)
img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)


# .astype(np.uint8)非常必须，调用cv2.cvtColor前必须转为uint8
img_pred = img_pred.astype(np.uint8)
img_pred_bgr = cv2.cvtColor(img_pred, cv2.COLOR_LAB2BGR)
img_pred_rgb = cv2.cvtColor(img_pred, cv2.COLOR_LAB2RGB)

# write BGR format
cv2.imwrite("a.jpg", img_pred_bgr)

# display RGB format
plt.imshow(img_pred_rgb)
plt.show()

#### plot_model

from keras.utils.vis_utils import plot_model
from IPython.display import Image, display
plot_model(model, to_file="/tmp/model.png", show_shapes=True)
display(Image('/tmp/model.png'))

#### Scikit-learn

from sklearn.model_selection import train_test_split
train, val = train_test_split(data, test_size=0.3)
X_train, X_val, y_train, y_val = train_test_split(X_all, y_all, test_size = 0.3)

from sklearn.model_selection import StratifiedKFold
cv = StratifiedKFold(n_splits=3, shuffle=True)

from sklearn.model_selection import cross_val_score
score = cross_val_score(LogisticRegression(), X_all, y_all, scoring='neg_mean_squared_error', cv=cv).mean()
score = cross_val_score(LogisticRegression(), X_all, y_all, scoring='accuracy', cv=cv).mean()

#### Learning Curve

from scikitplot import plotters as skplt
skplt.plot_learning_curve(LogisticRegression(), X_all, y_all)
plt.show()
skplt.plot_roc_curve(y_true=y_val, y_probas=y_proba)
plt.show()
skplt.plot_precision_recall_curve(y_true=y_val, y_probas=y_proba)
plt.show()
skplt.plot_confusion_matrix(y_true=y_val, y_pred=y_pred, normalize=True)
plt.show()

#### XGBoost

from xgboost import XGBRegressor
import xgboost as xgb
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
}
dtrain = xgb.DMatrix(X_all, label=y_all)
history = xgb.cv(params, dtrain, num_boost_round=1024, early_stopping_rounds=5, verbose_eval=20)

booster = xgb.train(params, dtrain)
xgb.plot_importance(booster=booster)
xgb.plot_tree(booster=booster)
xgb.to_graphviz(booster=booster)

#### StandardScaler

from sklearn.preprocessing import StandardScaler
std = StandardScaler()
X_all[:] = std.fit_transform(X_all)

#### GridSearchCV

from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_estimators': [60, 70, 80, 90],
    'learning_rate': [2, 3, 4, 5]
}
gs = GridSearchCV(
    AdaBoostRegressor(),
    param_grid = param_grid
)
gs.fit(X_all, y_all)
gs.best_params_

#### Keras

from keras.layers import Conv2D, Conv2DTranspose, BatchNormalization, MaxPooling2D, UpSampling2D, Lambda
from keras.models import Model, Input
from keras.callbacks import Callback, TensorBoard, ModelCheckpoint, EarlyStopping
import keras.backend as K

def my_loss():
    cross_entropy = K.categorical_crossentropy(y_pred, y_true)
    cross_entropy = K.mean(cross_entropy, axis=-1)
    return cross_entropy

def get_model():
    img_input = Input(shape=(IMG_HEIGHT, IMG_WIDTH, 1))
    x = img_input
    print(x.get_shape())

    x = Dense(32, activation='relu')(x)
    x = Conv2D(filters=64, kernel_size=3, strides=1, padding='same', activation='relu')(x)
    x = BatchNormalization()(x)
    x = UpSampling2D(size=2)(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Flatten()(x)
    x = Dropout(0.25)(x)
    x = Reshape(target_shape=(int(conv_shape[1]), int(conv_shape[2]*conv_shape[3])))(x)

    model.add(LSTM(LSTM_UNITS, input_shape=(SEN_LEN, len(all_chars)), return_sequences=True))
    model.add(LSTM(LSTM_UNITS, input_shape=(SEN_LEN, len(all_chars)), return_sequences=False))

    gru_1 = GRU(rnn_size, return_sequences=True, kernel_initializer='he_normal')(x)
    gru_1b = GRU(rnn_size, return_sequences=True, go_backwards=True, kernel_initializer='he_normal')(x)
    # keras.layers.add
    gru1_merged = add([gru_1, gru_1b])

    x = K.reshape(x, (-1, AB_PAIRS))
    x = K.softmax(x)
    x = K.resize_images(x, IMG_HEIGHT / curr_height, IMG_WIDTH / curr_width, data_format="channels_last")

    x = Lambda(lambda z: reshape(z), output_shape=(IMG_HEIGHT, IMG_WIDTH, AB_PAIRS))(x)

    model = Model(inputs=img_input, outputs=x)
    model.compile(loss='categorical_crossentropy', optimizer='Adadelta', metrics=['accuracy'])

model.load_weights('/input/Captcha/checkpoint-33-0.3923.hdf5')

class MyEvaluator(Callback):
    def __init__(self):
        self.gen = gen(1, random_choose=True)
    
    # self.model integrated
    def on_epoch_end(self, epoch, logs=None):
        X_test, y_test = next(self.gen) # (1, 128, 128, 1)
        y_pred = self.model.predict(X_test) # (1, 128, 128, AB_PAIRS)

model = get_model()
print('model built')

RUN = RUN + 1 if 'RUN' in locals() else 1
print("RUN {}".format(RUN))

LOG_DIR = '/output/training_logs/run-{}'.format(RUN)
LOG_FILE_PATH = LOG_DIR + '/checkpoint-{epoch:02d}-{val_loss:.4f}.hdf5'

tensorboard = TensorBoard(log_dir=LOG_DIR, write_images=True)
checkpoint = ModelCheckpoint(filepath=LOG_FILE_PATH, monitor='val_loss', verbose=1, save_best_only=True)
early_stopping = EarlyStopping(monitor='val_loss', patience=4, verbose=1)
evaluator = MyEvaluator()

history = model.fit_generator(generator=gen(8), steps_per_epoch=64,
                              validation_data=gen(8, random_choose=True), validation_steps=8,
                              epochs=10000, verbose=1, callbacks=[tensorboard, checkpoint, early_stopping, evaluator])

#### ImageDataGenerator

from keras.preprocessing.image import ImageDataGenerator

train_gen = ImageDataGenerator(data_format='channels_last').flow_from_directory(
    './train/', target_size=(IMG_WIDTH, IMG_HEIGHT), batch_size=BATCH_SIZE,
    class_mode='categorical', shuffle=True)

keras.preprocessing.image.ImageDataGenerator(featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    rotation_range=0.,
    width_shift_range=0.,
    height_shift_range=0.,
    shear_range=0.,
    zoom_range=0.,
    channel_shift_range=0.,
    fill_mode='nearest',
    cval=0.,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=K.image_data_format())

#### TensorFlow

# refer to: 
# RecommendSystem.ipynb
# DigitRecognizer_tensorflow.ipynb

import tensorflow as tf

# placeholder & Variable
a = tf.placeholder(dtype=tf.float32, shape=(BATCH_SIZE, IMAGE_PIXELS), name='input_images')
b = tf.constant(train_matrix, dtype=tf.float32, name='const_name')
b_bool = tf.cast(tf_train_matrix, dtype=tf.bool, name='cast_name')
c = tf.Variable(train_matrix, dtype=tf.float32, name='v_name')

# calculation
with tf.name_scope('hidden1'):
  pred_matrix = tf.tensordot(tf_user_features, tf_item_features, axes=[[1], [1]])
  pred_matrix_int = tf.cast(tf.round(pred_matrix), tf.int32)
  train_squared_diff_filtered = tf.where(tf_train_matrix_bool, tf.square(train_diff), tf_matrix_mean)

# loss definition and scalar record
loss = 0.1 * tf.sqrt(tf.reduce_sum(train_squared_diff_filtered))
tf.summary.scalar('loss', loss)

# Evaluation
evaluation_op = tf.reduce_sum(tf.where(tf_val_matrix_bool, tf.abs(val_diff), tf_matrix_zero_float)) / 20000
tf.summary.scalar('evaluation_value', evaluation_op)

# train operation
train_op = tf.train.GradientDescentOptimizer(learning_rate=1).minimize(loss)

# summary
summary_op = tf.summary.merge_all()

# session
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())

  # saver & summary_writer
  saver = tf.train.Saver()
  summary_writer = tf.summary.FileWriter("./log2/", sess.graph)

  for step in range(102400):
      feed_dict = {
          'placeholder1': <value>,
          'placeholder2': <value>,
      }
      _, loss_value = sess.run([train_op, loss], feed_dict=feed_dict)

      if (step + 1) % 128 == 0:
          # 其实scalar里面已经记录了，这里可以认为是一个自定义evaluator
          evaluation_score = sess.run(evaluation_op, feed_dict=feed_dict)
          saver.save(sess, "./log/cp-file.ckpt", global_step=step)

      if some-cond:
          summary_str = sess.run(summary_op, feed_dict=feed_dict)
          summary_writer.add_summary(summary_str, step)
          summary_writer.flush()

#### keras tensorflow
# ref to StyleTransfer.ipynb

#### Embedding
# ref to: MNIST/Embeddings.ipynb

只要存在Embeddings，Keras会自动记录。TB里会直接看到。我只需要手动生成meta-data文件，不管是程序中绑定，还是在TB中Load都可以。至于meta-data文件，提前生成也OK，程序生成也OK。

#### NPL, NLTK, ngrams
# ref to: Quora/Quora-neural-network.ipynb
# ref to: Quora/Quora-Feature-Enginnering.ipynb

#### word2vec
from gensim.models.word2vec import Word2Vec, KeyedVectors
word2vec = KeyedVectors.load_word2vec_format('/input/Kaggle/Word2Vec/GoogleNews-vectors-negative300.bin.gz', binary=True)
'apple' in word2vec.vocab # True

#### Tokenizer-Scikit-Learn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem.snowball import EnglishStemmer

# 自定义analyzer，加入stem
count_analyzer = CountVectorizer().build_analyzer()
stemmer = EnglishStemmer()

def stem_count_analyzer(doc):
    return (stemmer.stem(w) for w in count_analyzer(doc))

cv = CountVectorizer(analyzer=stem_count_analyzer, preprocessor=None, stop_words='english', max_features=128)
cv.fit(unique_questions)
q1_cv = cv.transform(train.question1)

# 使用默认word analyzer。再加入preprocessor
def preprocessor(review):
    return BeautifulSoup(review, 'html5lib').get_text()
count_v = CountVectorizer(analyzer='word', preprocessor=preprocessor, stop_words='english', max_features=5000)

#### Keras Tokenizer

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words=NUM_WORDS)
tokenizer.fit_on_texts(all_unique_questions)

q1_seq = tokenizer.texts_to_sequences(train.question1)
q1_seq_pad = pad_sequences(q1_seq, maxlen=MAX_SEQ_LEN)

input_size = len(tokenizer.word_index) + 1 # 0 index is all 0
shared_embedding = Embedding(input_dim=input_size, output_dim=EMBEDDING_DIM, input_length=MAX_SEQ_LEN,
                                weights=[embedding_weights], trainable=False, name='shared_embedding_layer')

# N-grams

from nltk.util import ngrams
ngrams([1,2,3,4,5], 2)

#### KMeans, MiniBatchKMeans, DBSCAN
# ref to: Iris/algorithm.ipynb

from sklearn.cluster import KMeans, MiniBatchKMeans, DBSCAN

kmeans = KMeans(n_clusters=5000, max_iter=10, n_jobs=8)
kmeans.fit(X_all)
X_all_km_centroids = [kmeans.cluster_centers_[idx] for idx in kmeans.labels_]

minibatchkmeans = MiniBatchKMeans(n_clusters=5000, max_iter=10)
minibatchkmeans.fit(X_all)
X_all_mbkm_centroids = [minibatchkmeans.cluster_centers_[idx] for idx in minibatchkmeans.labels_]

dbscan = DBSCAN()
dbscan.fit(X_all)
len(X_all), len(dbscan.core_sample_indices_), len(dbscan.components_), len(dbscan.labels_)

#### get_file

from keras.utils import get_file
path = get_file('nietzsche.txt', origin="https://s3.amazonaws.com/text-datasets/nietzsche.txt")
with open(path, 'r') as f:
  data = f.read()

#### tqdm

from tqdm import tqdm
for i in tqdm(range(100)):
  pass

#### glob

from glob import glob
file_glob = glob('{}/*.jpg'.format(DATA_DIR))

#### Thread

from threading import Thread

def handle_img(**kwargs):
    i = kwargs['i']

threads = []
for i in range(batch_size):
    kwargs = {
        'i': i,
    }
    t = Thread(target=handle_img, kwargs=kwargs)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

#### Logging

import logging
logger = logging.getLogger('log')
logger.setLevel(logging.WARNING)
logger.debug('abc')
logger.info('abc')
logger.warning('abc')
logger.error('abc')
logger.critical('abc')
logger.log('abc')
logger.exception('abc')

#### BeautifulSoup

from bs4 import BeautifulSoup
BeautifulSoup("<p>hello,workd</p>", 'html5lib').get_text()

#### time

from time import sleep
sleep(.5)

#### Arrow

import arrow

def parse_date(date_str, str_format='YYYY/MM/DD'):
    d = arrow.get(date_str, str_format)
    # 月初，月中，月末
    month_stage = int((d.day-1) / 10) + 1
    return (d.timestamp, d.year, d.month, d.day, d.week, d.isoweekday(), month_stage)

#### hypertools
# ref to: Iris/visualization.ipynb

import hypertools as hyp

hyp.plot(iris_with_centroid.drop('Species', axis=1), 'o', 
         group=iris_with_centroid.Species, 
         legend=list(set(iris_with_centroid.Species)))

