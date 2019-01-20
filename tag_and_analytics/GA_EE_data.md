# GA 향상된 전자상거래(EE)

- - -

## Data - key and value
1. Impression Data
2. Product Data
3. Promotion Data
4. Action Data

- - -

### 1. Impression Data
+ id
+ name
+ list
+ brand
+ category
+ variant
+ position(int)
+ price
> *id or name must be set.

- - -

### 2. Product Data
+ id
+ name : 예)고퍼후드티
+ brand : 예)아디다스오리지날
+ category : 예)의류
+ variant : 예)검정
+ price
+ quantity(int)
+ coupon : 예)뉴이어2019
+ position(int)
> *id or name must be set.

- - -

### 3. Promotion Data
+ id
+ name
+ creative
+ position
> *id or name must be set.

- - -

### 4. Action Data
+ id
+ affiliation
+ revenue
+ tax
+ shipping
+ coupon
+ list
+ step(int)
+ option
> *id: Required if the action type is purchase or refund.

- - -

### @ 참조링크들
+ [EE 참조](https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce)
+ [필드 레퍼런스](https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference)