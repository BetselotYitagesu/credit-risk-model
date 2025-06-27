# credit-risk-model

### Credit Scoring Business Understanding

1. Basel II Accord and Model Interpretability

The Basel II Accord emphasizes accurate risk measurement and capital adequacy to ensure financial stability. This requirement directly impacts how credit risk models must be developed. Specifically, models must be interpretable, transparent, and auditable, enabling financial institutions to explain risk predictions to regulators and stakeholders. An interpretable model facilitates trust, governance, and compliance, ensuring that risk-based decisions can be justified and that the model’s logic aligns with regulatory expectations.

2. The Need for a Proxy Variable and Business Risks

In our dataset, there is no direct label indicating loan default, which is a standard requirement for supervised credit risk modeling. Therefore, we must engineer a proxy target variable that reasonably approximates default behavior. For example, clustering disengaged customers based on Recency, Frequency, and Monetary (RFM) activity can serve as a proxy for risk.

However, this introduces business risks, such as:

    Mislabeling risk: Some customers labeled as "high risk" may not actually default.

    Bias amplification: If the proxy is poorly defined, the model could reinforce incorrect assumptions.

    Regulatory exposure: Models based on synthetic or proxy targets may not hold up to regulatory scrutiny unless justified with clear reasoning and validation.

3. Model Trade-offs: Simplicity vs Performance

There is a critical trade-off between simple, interpretable models and complex, high-performance models:

Model Trade-offs: Simplicity vs Performance

    Logistic Regression with WoE

        ✅ Pros:
            Highly interpretable
            Transparent decision rules
            Easy to validate and explain to regulators

        ❌ Cons:
            May underperform on complex patterns
            Lower predictive power

    Gradient Boosting (e.g., XGBoost, LightGBM)

        ✅ Pros:
            High predictive accuracy
            Captures non-linear relationships and feature interactions

        ❌ Cons:
            Less interpretable (black-box behavior)
            Harder to explain to stakeholders
            Greater risk of regulatory scrutiny

**_ In regulated financial contexts, the choice depends on the balance between predictive power and the need for transparency, fairness, and compliance. Often, interpretable models are preferred in production while complex models may support internal analysis. _**
