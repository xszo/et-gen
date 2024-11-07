NULL = "https://cdn.jsdelivr.net/gh/xszo/etc@etc/null"


def proxy(out) -> None:
    out.writelines(
        [
            x + "\n"
            for x in [
                "[custom]",
                "ruleset=DIRECT,[]FINAL",
                "custom_proxy_group=Node`select`[]DIRECT`[]REJECT",
                "add_emoji=false",
                "clash_rule_base=" + NULL,
                "loon_rule_base=" + NULL,
                "mellow_rule_base=" + NULL,
                "quan_rule_base=" + NULL,
                "quanx_rule_base=" + NULL,
                "singbox_rule_base=" + NULL,
                "sssub_rule_base=" + NULL,
                "surfboard_rule_base=" + NULL,
                "surge_rule_base=" + NULL,
                "rename=^(JMS-\\d+).(c\\d+s[123])\\..*@$1 $2 US",
                "rename=^(JMS-\\d+).(c\\d+s4)\\..*@$1 $2 JP",
                "rename=^(JMS-\\d+).(c\\d+s5)\\..*@$1 $2 NL",
                "rename=^(JMS-\\d+).(c\\d+s\\d+)\\..*@$1 $2",
            ]
        ]
    )
