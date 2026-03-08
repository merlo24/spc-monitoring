from spc_monitor.charts.mwd2_location import MWD2LocationChart


_CHARTS = {
    "mwd2_location": MWD2LocationChart,
}


def control_chart(data, chart="mwd2_location", **kwargs):
    chart = str(chart).lower().strip()
    if chart not in _CHARTS:
        raise ValueError(f"Unknown chart='{chart}'. Available: {list(_CHARTS)}")

    cls = _CHARTS[chart]
    return cls.fit(reference=data, **kwargs)