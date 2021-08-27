# Customer Segmentation via Cluster Analysis

## Project Overview
Using Machine Learning Modeling to perform customer segmentation via cluster analysis and make data-driven business decisions.

## Motivation

# Customer Segmentation via Cluster Analysis

## Project Overview
Using Machine Learning Modeling to perform customer segmentation via cluster analysis and make data-driven business decisions.

### What is Customer Segmentation?
The practice of dividing customer data into groups that reflect the similarities amongst customers.  Segmentation is also referred to as clustering.  These homoegeneous groups (segments/clusters) are sometimes referred to as "*customer archetypes*" or "*personas*".

### Why do it?
Businesses may **become more customer centric** and gain a sustainable **competitive advantage** by understanding how to relate to different customers in order to maximize the value of each customer to the business.
An accurate segmentation will allow for more effective customer marketing via personalization.  This helps to maximize the effectiveness of every contact with each customer.

This could increase Return on Investment (ROI) of marketing actions by increasing the number of customers (through better retention/reduced churn but also adoption) and/or increasing customer spend.  Marketing actions include campaigns, offers, incentives, upgrades, etc.

### Different Segmentation approaches
The segments are commonly marketer-designed and hard coded (threshold or rule-based segmentation).  Based on the experience and assumptions of a marketer, a priori threshold is selected, typically in 2-D.  The disadvantage of this is that the predetermined thresholds will often result in results that meet the initial assumptions.  We will often not learn anything from the data.  Additionally it is common to see a large variance amongst customers in the same segment, and going beyond 2-D is fairly difficult.

A better approach is to use machine learning (ML) models with an analytical segmentation.  The advanced mathematical algorithms will produce segmentations and insights which would have been difficult to discover in a marketer-designed approach.  A second benefit is that we can keep on improving these segments.  ML segmentation models create a feedback loop, whereby an accurate model will guide new marketing actions.  The performance of these actions can then be analyzed to improve the next iteration of model.  The ML approach can create segments over many dimensions (customer variables) which results in a lower variance within each segment.  A common ML model to use for clustering is K-Means Clustering.

### Dynamic Clustering
Clusters often change over time and with an ML approach the customer segmentation can be updated easily and frequently (ideally daily) to give an accurate representation of the current state of customers.

### Macro vs Micro Segmentation
Macro - high level data, e.g. location, language.  Result is large segments with higher level of heterogeneity, which makes it harder to effectively personalize marketing actions.
Micro - Specific data, e.g. preferred service, history with the business, time since last purchase.  Result is smaller segments that have more homogenous customers, which makes it easier to effectively personalize marketing actions (e.g. send a time-limited coupon to encourage a customer to return).

Often a Macro-segmentation approach is initially used to gain a broad understanding of the customer base.  The Micro-segmentation will then be used to guide the marketing actions.

### Lifecycle Stages
Customers may be segmented into six lifecycle stages: fun, new, active, star, churn and reengaged

### Customer Migration between Segments
It should be noted that customers will move between segments over time.  The path that this customer took can help to improve the accuracy of cluster analysis

## Marketing KPIs

### Customer Lifetime Value
How much a customer generates for the business
This represents the health of the customer base and the growth potential
It is the Net Present Value (NPV) of future cash flows from any customer
Results in leaving no customer behind, long-term customer loyalty, improved brand perception, maximum customer value 

### Customer Satisfaction (CSAT)
Star Rating, and different to NPS
easy to interpret for customers, however it is not linear.  a 4.8/5 is deemed to be optimal . anything above raises suspicion for legitimacy.
Helps to track brand perception

### Churn Rate
This is expressed as a % in a time period, or the revenue lost


## Project Structure

1) Identify Business Issues
    a) Which Customers are our biggest spenders?
    b) Which Previously Big Customers have not purchased anything recently?
2) Generate Hypotheses
3) Decide on Data to Collect
4) Gather Data
5) Clean Data
6) Build Segmentation Models
7) Analysis of Segmentation (similar attributes, % of total population, perceptual maps)
8) Link to Business Strategy (Marketing).  Identify opportunities and KPIs

## Screenshots & Charts

## Code Example

## Installation

## How to use
The virtual environment for this project has been saved in the spec-file.txt.  To recreate this project, simply clone the project to a local machine and assuming you have Conda installed, run the following from the command line in the project's home directory:
>> conda create --name mynewenvname --file spec-file.txt


## Credits
