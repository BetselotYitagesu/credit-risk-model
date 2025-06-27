## 📊 Credit Scoring Business Understanding

In regulated financial services, credit scoring models must balance predictive performance with transparency, fairness, and compliance. This project is guided by key considerations from the Basel II Accord and the unique data constraints we face—such as the absence of direct default labels. This section summarizes the business and regulatory context for building a responsible and robust credit scoring model.

### 1. Basel II Accord and the Need for Interpretability

The Basel II Capital Accord requires financial institutions to quantify and document risk exposures using sound, explainable methods. As a result, credit risk models must be interpretable and auditable. Building a well-documented model that clearly shows how risk is estimated ensures regulatory compliance, builds institutional trust, and enables human oversight in decision-making.

### 2. The Role of Proxy Variables and Associated Risks

Since the dataset lacks a direct "default" label (i.e., no clear indicator of whether a customer failed to repay), we must create a **proxy variable** to estimate credit risk. This involves clustering behavioral data—like Recency, Frequency, and Monetary value (RFM)—to label disengaged users as "high risk".

However, using a proxy comes with business risks:

- **Misclassification:** Customers may be incorrectly labeled, affecting real-world credit decisions.
- **Bias amplification:** A poorly defined proxy can introduce or reinforce systemic bias.
- **Regulatory scrutiny:** Proxies must be carefully justified; unjustified proxies may not pass compliance reviews.

### 3. Trade-offs Between Simple and Complex Models

- **Logistic Regression with Weight of Evidence (WoE)**

  - ✅ Pros:
    - Highly interpretable and transparent
    - Easy to explain to regulators and stakeholders
    - Well-aligned with traditional credit scoring methods
  - ❌ Cons:
    - May fail to capture complex patterns in customer behavior
    - Lower predictive accuracy in some cases

- **Gradient Boosting Models (e.g., XGBoost, LightGBM)**
  - ✅ Pros:
    - High predictive power
    - Captures complex, non-linear feature interactions
  - ❌ Cons:
    - Opaque decision logic ("black-box" models)
    - Difficult to interpret and justify in high-stakes, regulated environments
    - Increased risk of non-compliance

In financial applications, the model choice depends on balancing **accuracy** with **interpretability**. Often, interpretable models are prioritized in production, while complex models may support internal analytics and insights.
