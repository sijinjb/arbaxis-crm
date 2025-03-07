"""
URL configuration for crms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from apps import views as app_views
from components import views as components_views
from dashboard import views as dashboard_views
from django.conf.urls.static import static


urlpatterns = [
    path('crms/template/admin/', admin.site.urls),

    # Dashboard
    
    path('crms/template/dashboard', dashboard_views.index, name='index'),
    path('crms/template/leads-dashboard', dashboard_views.leads_dashboard, name='leads_dashboard'),
    path('crms/template/project-dashboard', dashboard_views.project_dashboard, name='project_dashboard'),
    
    #Layouts
    path('crms/template/layout-mini', app_views.layout_mini, name='layout_mini'),
    path('crms/template/layout-horizontal-single', app_views.layout_horizontal_single, name='layout_horizontal_single'),
    path('crms/template/layout-without-header', app_views.layout_without_header, name='layout_without_header'),
    path('crms/template/layout-rtl', app_views.layout_rtl, name='layout_rtl'),
    path('crms/template/layout-detached', app_views.layout_detached, name='layout_detached'),
    path('crms/template/layout-dark', app_views.layout_dark, name='layout_dark'),
    
    # Authentication

    path('', app_views.login, name='login'),
    path('crms/template/register', app_views.register, name='register'),
    path('crms/template/register', app_views.register, name='register'),
    path('crms/template/forgot-password', app_views.forgot_password, name='forgot_password'),
    path('crms/template/reset-password', app_views.reset_password, name='reset_password'),
    path('crms/template/email-verification', app_views.email_verification, name='email_verification'),
    path('crms/template/two-step-verification', app_views.two_step_verification, name='two_step_verification'),
    path('crms/template/lock-screen', app_views.lock_screen, name='lock_screen'),
    path('crms/template/success', app_views.success, name='success'),
    
    # pages
    
    path('crms/template/error-404', app_views.error_404, name="error_404"),
    path('crms/template/error-500', app_views.error_500, name="error_500"),
    path('crms/template/coming-soon', app_views.coming_soon, name="coming_soon"),
    path('crms/template/blank-page', app_views.blank_page, name="blank_page"),
    path('crms/template/under-maintenance', app_views.under_maintenance, name="under_maintenance"),
    
    # Reports
    
    path('crms/template/lead-reports' ,app_views.lead_reports ,name='lead_reports'),
    path('crms/template/deal-reports' ,app_views.deal_reports ,name='deal_reports'),
    path('crms/template/contact-reports' ,app_views.contact_reports ,name='contact_reports'),
    path('crms/template/company-reports' ,app_views.company_reports ,name='company_reports'),
    path('crms/template/project-reports' ,app_views.project_reports ,name='project_reports'),
    path('crms/template/task-reports' ,app_views.task_reports ,name='task_reports'),
    
    # Settings
    
    path('crms/template/profile', app_views.profile, name='profile'),
    path('crms/template/security', app_views.security, name='security'),
    path('crms/template/notifications', app_views.notifications, name='notifications'),
    path('crms/template/connected-apps', app_views.connected_apps, name='connected_apps'),
    
    path('crms/template/company-settings', app_views.company_settings, name='company_settings'),
    path('crms/template/localization', app_views.localization, name='localization'),
    path('crms/template/prefixes', app_views.prefixes, name='prefixes'),
    path('crms/template/preference', app_views.preference, name='preference'),
    path('crms/template/appearance', app_views.appearance, name='appearance'),
    path('crms/template/language', app_views.language, name='language'),
    path('crms/template/language-web', app_views.language_web, name='language_web'),
    
    path('crms/template/invoice-settings', app_views.invoice_settings, name='invoice_settings'),
    path('crms/template/printers', app_views.printers, name='printers'),
    path('crms/template/custom-fields', app_views.custom_fields, name='custom_fields'),
    
    path('crms/template/email-settings', app_views.email_settings, name='email_settings'),
    path('crms/template/sms-gateways', app_views.sms_gateways, name='sms_gateways'),
    path('crms/template/gdpr-cookies', app_views.gdpr_cookies, name='gdpr_cookies'),
    
    path('crms/template/payment-gateways', app_views.payment_gateways, name='payment_gateways'),
    path('crms/template/bank-accounts', app_views.bank_accounts, name='bank_accounts'),
    path('crms/template/tax-rates', app_views.tax_rates, name='tax_rates'),
    path('crms/template/currencies', app_views.currencies, name='currencies'),
    
    path('crms/template/storage', app_views.storage, name='storage'),
    path('crms/template/ban-ip-address', app_views.ban_ip_address, name='ban_ip_address'),
    
    # Supports
    
    path('crms/template/tickets' , app_views.tickets, name='tickets'),
    path('crms/template/contact-messages' , app_views.contact_messages, name='contact_messages'),
    
    # Pages
    
    path('crms/template/pages' , app_views.pages, name='pages'),
    path('crms/template/countries' , app_views.countries, name='countries'),
    path('crms/template/states' , app_views.states, name='states'),
    path('crms/template/cities' , app_views.cities, name='cities'),
    path('crms/template/testimonials' , app_views.testimonials, name='testimonials'),
    path('crms/template/faq' , app_views.faq, name='faq'),
    
    # Membership
    
    path('crms/template/membership-plans' , app_views.membership_plans, name='membership_plans'),
    path('crms/template/membership-addons' , app_views.membership_addons, name='membership_addons'),
    path('crms/template/membership-transactions' , app_views.membership_transactions, name='membership_transactions'),
    
    # User Management
    
    path('crms/template/manage-users' , app_views.manage_users, name='manage_users'),
    path('crms/template/roles-permissions' , app_views.roles_permissions, name='roles_permissions'),
    path('crms/template/permission' , app_views.permission, name='permission'),
    path('crms/template/delete-request' , app_views.delete_request, name='delete_request'),
    
    # CRM Settings
    path('crms/template/sources', app_views.sources, name='sources'),
    path('crms/template/lost-reason', app_views.lost_reason, name='lost_reason'),
    path('crms/template/contact-stage', app_views.contact_stage, name='contact_stage'),
    path('crms/template/industry', app_views.industry, name='industry'),
    path('crms/template/calls', app_views.calls, name='calls'),
    
    # UI Module
    
    path('crms/template/ui-alerts', components_views.ui_alerts, name='ui_alerts'),
    path('crms/template/ui-accordion', components_views.ui_accordion, name='ui_accordion'),
    path('crms/template/ui-avatar', components_views.ui_avatar, name='ui_avatar'),
    path('crms/template/ui-badges', components_views.ui_badges, name='ui_badges'),
    path('crms/template/ui-borders', components_views.ui_borders, name='ui_borders'),
    path('crms/template/ui-buttons', components_views.ui_buttons, name='ui_buttons'),
    path('crms/template/ui-buttons-group', components_views.ui_buttons_group, name='ui_buttons_group'),
    path('crms/template/ui-breadcrumb', components_views.ui_breadcrumb, name='ui_breadcrumb'),
    path('crms/template/ui-cards', components_views.ui_cards, name='ui_cards'),
    path('crms/template/ui-carousel', components_views.ui_carousel, name='ui_carousel'),
    path('crms/template/ui-colors', components_views.ui_colors, name='ui_colors'),
    path('crms/template/ui-dropdowns', components_views.ui_dropdowns, name='ui_dropdowns'),
    path('crms/template/ui-grid', components_views.ui_grid, name='ui_grid'),
    path('crms/template/ui-images', components_views.ui_images, name='ui_images'),
    path('crms/template/ui-lightbox', components_views.ui_lightbox, name='ui_lightbox'),
    path('crms/template/ui-media', components_views.ui_media, name='ui_media'),
    path('crms/template/ui-modals', components_views.ui_modals, name='ui_modals'),
    path('crms/template/ui-offcanvas', components_views.ui_offcanvas, name='ui_offcanvas'),
    path('crms/template/ui-pagination', components_views.ui_pagination, name='ui_pagination'),
    path('crms/template/ui-popovers', components_views.ui_popovers, name='ui_popovers'),
    path('crms/template/ui-progress', components_views.ui_progress, name='ui_progress'),
    path('crms/template/ui-placeholders', components_views.ui_placeholders, name='ui_placeholders'),
    path('crms/template/ui-spinner', components_views.ui_spinner, name='ui_spinner'),
    path('crms/template/ui-sweetalerts', components_views.ui_sweetalerts, name='ui_sweetalerts'),
    path('crms/template/ui-nav-tabs', components_views.ui_nav_tabs, name='ui_nav_tabs'),
    path('crms/template/ui-toasts', components_views.ui_toasts, name='ui_toasts'),
    path('crms/template/ui-tooltips', components_views.ui_tooltips, name='ui_tooltips'),
    path('crms/template/ui-typography', components_views.ui_typography, name='ui_typography'),
    path('crms/template/ui-video', components_views.ui_video, name='ui_video'),
    path('crms/template/ui-sortable', components_views.ui_sortable, name='ui_sortable'),
    path('crms/template/ui-swiperjs', components_views.ui_swiperjs, name='ui_swiperjs'),
        
    # Advanced UI  
    
    path('crms/template/ui-ribbon', components_views.ui_ribbon, name='ui_ribbon'),
    path('crms/template/ui-clipboard', components_views.ui_clipboard, name='ui_clipboard'),
    path('crms/template/ui-drag-drop', components_views.ui_drag_drop, name='ui_drag_drop'),
    path('crms/template/ui-rangeslider', components_views.ui_rangeslider, name='ui_rangeslider'),
    path('crms/template/ui-text-editor', components_views.ui_text_editor, name='ui_text_editor'),
    path('crms/template/ui-counter', components_views.ui_counter, name='ui_counter'),
    path('crms/template/ui-scrollbar', components_views.ui_scrollbar, name='ui_scrollbar'),
    path('crms/template/ui-stickynote', components_views.ui_stickynote, name='ui_stickynote'),
    path('crms/template/ui-timeline', components_views.ui_timeline, name='ui_timeline'),
    
    #Charts
    
    path('crms/template/chart-apex', components_views.chart_apex, name='chart_apex'),
    path('crms/template/chart-c3', components_views.chart_c3, name='chart_c3'),
    path('crms/template/chart-js', components_views.chart_js, name='chart_js'),
    path('crms/template/chart-morris', components_views.chart_morris, name='chart_morris'),
    path('crms/template/chart-flot', components_views.chart_flot, name='chart_flot'),
    path('crms/template/chart-peity', components_views.chart_peity, name='chart_peity'),
    
    #Icons
    
    path('crms/template/icon-fontawesome', components_views.icon_fontawesome, name='icon_fontawesome'),
    path('crms/template/icon-feather', components_views.icon_feather, name='icon_feather'),
    path('crms/template/icon-ionic', components_views.icon_ionic, name='icon_ionic'),
    path('crms/template/icon-material', components_views.icon_material, name='icon_material'),
    path('crms/template/icon-pe7', components_views.icon_pe7, name='icon_pe7'),
    path('crms/template/icon-simpleline', components_views.icon_simpleline, name='icon_simpleline'),
    path('crms/template/icon-themify', components_views.icon_themify, name='icon_themify'),
    path('crms/template/icon-weather', components_views.icon_weather, name='icon_weather'),
    path('crms/template/icon-typicon', components_views.icon_typicon, name='icon_typicon'),
    path('crms/template/icon-flag', components_views.icon_flag, name='icon_flag'),
    path('crms/template/icon-tabler', components_views.icon_tabler, name='icon_tabler'),
    path('crms/template/icon-bootstrap', components_views.icon_bootstrap, name='icon_bootstrap'),
    path('crms/template/icon-remix', components_views.icon_remix, name='icon_remix'),
    
    #Forms
    
    path('crms/template/form-basic-inputs', components_views.form_basic_inputs, name='form_basic_inputs'),
    path('crms/template/form-checkbox-radios', components_views.form_checkbox_radios, name='form_checkbox_radios'),
    path('crms/template/form-input-groups', components_views.form_input_groups, name='form_input_groups'),
    path('crms/template/form-grid-gutters', components_views.form_grid_gutters, name='form_grid_gutters'),
    path('crms/template/form-select', components_views.form_select, name='form_select'),
    path('crms/template/form-mask', components_views.form_mask, name='form_mask'),
    path('crms/template/form-fileupload', components_views.form_fileupload, name='form_fileupload'),
    path('crms/template/form-elements', components_views.form_elements, name='form_elements'),
    path('crms/template/form-horizontal', components_views.form_horizontal, name='form_horizontal'),
    path('crms/template/form-vertical', components_views.form_vertical, name='form_vertical'),
    path('crms/template/form-floating-labels', components_views.form_floating_labels, name='form_floating_labels'),
    path('crms/template/form-validation', components_views.form_validation, name='form_validation'),
    path('crms/template/form-select2', components_views.form_select2, name='form_select2'),
    path('crms/template/form-wizard', components_views.form_wizard, name='form_wizard'),
    path('crms/template/form-pickers', components_views.form_pickers, name='form_pickers'),
    
    # Tables
    
    path('crms/template/tables-basic', components_views.tables_basic, name='tables_basic'),
    path('crms/template/data-tables', components_views.data_tables, name='data_tables'),
    
    # Maps
    
    path('crms/template/maps-vector', components_views.maps_vector, name='maps_vector'),
    path('crms/template/maps-leaflet', components_views.maps_leaflet, name='maps_leaflet'),

    #   Application

    path('crms/template/chat', app_views.chat, name='chat'),
    path('crms/template/video-call', app_views.video_call, name='video_call'),
    path('crms/template/audio-call', app_views.audio_call, name='audio_call'),
    path('crms/template/call-history', app_views.call_history, name='call_history'),
    path('crms/template/calendar', app_views.calendar, name='calendar'),
    path('crms/template/email', app_views.email, name='email'),
    path('crms/template/todo', app_views.todo, name='todo'),
    path('crms/template/notes', app_views.notes, name='notes'),
    path('crms/template/file-manager', app_views.file_manager, name='file_manager'),
    path('crms/template/social-feed', app_views.social_feed, name='social_feed'),
    path('crms/template/kanban-view', app_views.kanban_view, name='kanban_view'),
    path('crms/template/invoices', app_views.invoices, name='invoices'),
    path('crms/template/invoice-details', app_views.invoice_details, name='invoice_details'),
    path('crms/template/dashboard', app_views.dashboard, name='dashboard'),
    path('crms/template/domain', app_views.domain, name='domain'),
    path('crms/template/company', app_views.company, name='company'),
    path('crms/template/packages', app_views.packages, name='packages'),
    path('crms/template/packages-grid', app_views.packages_grid, name='packages_grid'),
    path('crms/template/purchase-transaction', app_views.purchase_transaction, name='purchase_transaction'),
    path('crms/template/subscription', app_views.subscription, name='subscription'),

    #   CRM

    path('crms/template/contacts', app_views.contacts, name='contacts'),
    path('crms/template/contact-grid', app_views.contact_grid, name='contact_grid'),
    path('crms/template/contact-details', app_views.contact_details, name='contact_details'),
    path('crms/template/companies', app_views.companies, name='companies'),
    path('crms/template/companies-grid', app_views.companies_grid, name='companies_grid'),
    path('crms/template/company-details', app_views.company_details, name='company_details'),
    path('crms/template/deals', app_views.deals, name='deals'),
    path('crms/template/deals-kanban', app_views.deals_kanban, name='deals_kanban'),
    path('crms/template/deals-details', app_views.deals_details, name='deals_details'),
    path('crms/template/leads', app_views.leads, name='leads'),
    path('crms/template/add_lead',app_views.add_lead, name='add_lead'),
    path('crms/template/leads-details', app_views.leads_details, name='leads_details'),
    path('crms/template/pipeline', app_views.pipeline, name='pipeline'),
    path('crms/template/campaign', app_views.campaign, name='campaign'),
    path('crms/template/campaign-complete', app_views.campaign_complete, name='campaign_complete'),
    path('crms/template/campaign-archieve', app_views.campaign_archieve, name='campaign_archieve'),
    path('crms/template/projects', app_views.projects, name='projects'),
    path('crms/template/project-grid', app_views.project_grid, name='project_grid'),
    path('crms/template/project-details', app_views.project_details, name='project_details'),
    path('crms/template/tasks', app_views.tasks, name='tasks'),
    path('crms/template/tasks-important', app_views.tasks_important, name='tasks_important'),
    path('crms/template/tasks-completed', app_views.tasks_completed, name='tasks_completed'),
    path('crms/template/proposals', app_views.proposals, name='proposals'),
    path('crms/template/proposals-grid', app_views.proposals_grid, name='proposals_grid'),
    path('crms/template/contracts', app_views.contracts, name='contracts'),
    path('crms/template/contracts-grid', app_views.contracts_grid, name='contracts_grid'),
    path('crms/template/estimations', app_views.estimations, name='estimations'),
    path('crms/template/estimations-kanban', app_views.estimations_kanban, name='estimations_kanban'),
    path('crms/template/invoices', app_views.invoices, name='invoices'),
    path('crms/template/invoice-grid', app_views.invoice_grid, name='invoice_grid'),
    path('crms/template/payments', app_views.payments, name='payments'),
    path('crms/template/analytics', app_views.analytics, name='analytics'),
    path('crms/template/activities', app_views.activities, name='activities'),
    path('crms/template/activity-calls', app_views.activity_calls, name='activity_calls'),
    path('crms/template/activity-mail', app_views.activity_mail, name='activity_mail'),
    path('crms/template/activity-task', app_views.activity_task, name='activity_task'),
    path('crms/template/activity-meeting', app_views.activity_meeting, name='activity_meeting'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
