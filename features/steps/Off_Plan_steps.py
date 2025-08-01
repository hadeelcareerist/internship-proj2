from behave import given, when, then


@given('I open the Reelly site')
def step_open_site(context):
    context.app.login_page.open_login_page()


@when('I log in')
def step_login(context):
    context.app.login_page.login("hadeel.altameemi@gmail.com", "Hadoola@2hm")


@when('I go to the Off-plan page')
def step_go_to_off_plan(context):
    context.app.menu.go_to_off_plan()
#Mobile
@when('I go to the Off-plan page on mobile')
def step_go_to_off_plan_mobile(context):
    context.app.menu.go_to_off_plan_mobile()

@when('I go to the Secondary page')
def step_go_to_secondary(context):
    context.app.menu.go_to_secondary()

@when('I go back to the Off-plan page')
def step_go_back_to_off_plan(context):
    context.app.menu.go_back_to_off_plan()

@when('I go back to the Off-plan mobile page')
def step_go_back_to_off_plan_mobile(context):
    context.app.menu.go_back_to_off_plan_mobile()


@then('I should be on the off plan page')
def step_verify_page(context):
    context.app.off_plan.verify_off_plan_page()

@then ('I should be on the off plan mobile page')
def step_verify_mobile_off_plan(context):
    context.app.off_plan.verify_off_plan_page_mobile()

@when('I go to the final page using the pagination button')
def step_pagination_next(context):
    context.app.off_plan.go_to_final_page()

@when ('I go to the final page mobile using the pagination button')
def step_pagination_next_mobile(context):
    context.app.off_plan.go_to_final_page_mobile()


@when('I go back to the first page using the pagination button')
def step_pagination_prev(context):
    context.app.off_plan.go_to_first_page()

@when('I go back to the first page mobile using the pagination button')
def step_pagination_prev_mobile(context):
    context.app.off_plan.go_to_first_page_mobile()
