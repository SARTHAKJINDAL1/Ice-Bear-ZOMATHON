def calculate_aov_lift(
    baseline_attach,
    new_attach,
    avg_addon_value,
    daily_orders
):
    incremental_rate=new_attach-baseline_attach
    incremental_addons=incremental_rate*daily_orders
    revenue_lift=incremental_addons*avg_addon_value
    return revenue_lift
lift = calculate_aov_lift(
    baseline_attach=0.12,
    new_attach=0.16,
    avg_addon_value=80,
    daily_orders=1000000
)
print("Projected Daily Revenue Lift:", lift)