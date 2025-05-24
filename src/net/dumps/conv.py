from ...ren import EMPTY


def proxy(out) -> None:
    out.writelines(
        [
            x + "\n"
            for x in [
                "[custom]",
                "enable_rule_generator=true",
                "overwrite_original_rules=true",
                "ruleset=DIRECT,[]FINAL",
                #
                "custom_proxy_group=ON`select`[]DIRECT`[]REJECT",
                #
                "rename=^(JMS-\\d+).(c\\d+s[123])\\..*@$1 $2 US",
                "rename=^(JMS-\\d+).(c\\d+s4)\\..*@$1 $2 JP",
                "rename=^(JMS-\\d+).(c\\d+s5)\\..*@$1 $2 NL",
                "rename=^(JMS-\\d+).(c\\d+s\\d+)\\..*@$1 $2",
                #
                "clash_rule_base=" + EMPTY,
                "loon_rule_base=" + EMPTY,
                "mellow_rule_base=" + EMPTY,
                "quan_rule_base=" + EMPTY,
                "quanx_rule_base=" + EMPTY,
                "singbox_rule_base=" + EMPTY,
                "sssub_rule_base=" + EMPTY,
                "surfboard_rule_base=" + EMPTY,
                "surge_rule_base=" + EMPTY,
                #
                "remove_old_emoji=false",
            ]
        ]
    )
