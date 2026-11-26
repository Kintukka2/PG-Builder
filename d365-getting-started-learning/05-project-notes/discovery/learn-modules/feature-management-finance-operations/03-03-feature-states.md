<!-- https://learn.microsoft.com/en-us/training/modules/feature-management-finance-operations/03-feature-states -->
# Feature states

Completed

* 10 minutes

Features can transition between several states, from being introduced in Feature management to eventually becoming mandatory in the product. This section describes the valid feature states.

### Preview features (optional)

Product teams can decide to initially start a new feature as a preview feature. Preview features aren't enabled by default and are optional. The owning product team will update features to **Released** after they have completed a successful preview period.

Note

Preview features are subject to specific preview [terms and conditions](https://go.microsoft.com/fwlink/?linkid=2105274).

### Released features (optional)

The **Feature state** column for released features is blank. Features that are initially added as released aren't turned on by default and enabling them is optional. Features that are updated from **Preview** will keep their enablement status.

### On by default features (optional)

Features that are updated to **On by default** are turned on by default, but you can disable them. After features that can be disabled have been in the **Released** state for at least six months, they are expected to move to this state in the next major release. Features that transition to **On by default** should be communicated in the [What's new](/en-us/dynamics365/fin-ops-core/fin-ops/get-started/whats-new-changed/?azure-portal=true) topic for the release. The update is initiated by the owning product team.

Note

Because these features will be enabled automatically, you need to determine whether your organization is ready to uptake these features or whether more time is necessary. If more time is needed, you might be required to temporarily disable these features. The transition of a feature to **On by default** is typically done in the major release before the feature is targeted to become **Mandatory**. At that point, you won't have the option to disable the feature.

### Released features (mandatory)

**Released** is the final state for features. It indicates that the features are turned on and that you can't disable them without contacting Microsoft. Optional features are expected to become mandatory after two major releases. Critical features can, by exception, be introduced as mandatory.

## Example of expected feature life cycles

Features that can be disabled, and that were added as released and optional before or as part of the April release, are expected to transition to **On by default** in the following October release. Then, they are expected to become **Mandatory** in April of the following year.

Features that can't be disabled, and that were added as released and optional before or as part of the April release, are expected to transition to **Mandatory** in April of the following year.