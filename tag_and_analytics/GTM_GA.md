# GTM - GA


## \# ga()
1. create
2. require
3. setAction
4. send

- - -

### 1. create
+ Tracker의 생성
+ ex)
```js
ga('create', {
  trackingId: 'UA-XXXXX-Y',
  cookieDomain: 'auto',
  name: 'myTracker',
  userId: '12345'
});
```
or
```js
ga('create', 'UA-XXXXX-Y', 'auto', 'myTracker', {
  userId: '12345'
});
```
+ [create 참조링크](https://developers.google.com/analytics/devguides/collection/analyticsjs/creating-trackers)

- - -
### 2. require
+ Plugins 이용하기
	- ec, displayfeatures,linkTracker ...
+ ex)
```js
ga('require', 'ec');
```
+ [require 참조링크](https://developers.google.com/analytics/devguides/collection/analyticsjs/using-plugins)

- - -
### 3. setAction
+ 3-1. Actions (Product and Promotion)
	- detail
		* 제품상세봄 
		* GA-Ec-Shopping-ProductViews
	- add
	 	* 쇼핑카트에제품(들)추가
		* GA-Ec-Shopping-AddToCart
	- checkout
	 	* 결제진행
		* GA-Ec-Shopping-Checkout
	- purchase
		* 판매
		* GA-Ec-Shopping-Transactions
	- click
	- remove
	- chekcout_option
	- refund
	- promo_click 

- - -
### 4. send
+ GA로 데이터 보내기
+ method reference
	- pageview
	- event
	- social
	- timing

+ ex)
```js
ga('send', {
  hitType: 'event',
  eventCategory: 'Video',
  eventAction: 'play',
  eventLabel: 'cats.mp4'
});
```
or
```js
ga('send', 'event', 'Video', 'play', 'cats.mp4');
```
or
```js
ga(function(tracker) {
  tracker.send('event', 'Video', 'play', 'cats.mp4');
});
```
+ [send 참조링크](https://developers.google.com/analytics/devguides/collection/analyticsjs/command-queue-reference#send)