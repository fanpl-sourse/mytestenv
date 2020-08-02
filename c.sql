
-- ========================================================================================
-- 经纪公司商服维度业务动作统计
-- Script Name  : edw_agents.adm_edw_company_staff_business_behavior_statistics_report_df.sql
--
-- Source Table : --
--
-- Target Table : edw_agents.adm_edw_company_staff_business_behavior_statistics_report_df
--
-- --------------------------------- Change Log -------------------------------------------
-- Date Generated   Updated By     Description
-- ----------------------------------------------------------------------------------------
-- 2020-07-16       denghong    Initial Version
-- ========================================================================================

insert overwrite table edw_agents.adm_edw_company_staff_business_behavior_statistics_report_df partition(dt='${dt}')
select
         to_date(from_unixtime(unix_timestamp('${dt}','yyyyMMdd')))         as statistic_date
        ,data_table.company_id                                             as company_id
        ,staff_table.staff_id                                               as staff_id
        ,staff_table.organization_id                                        as organization_id
        ,staff_table.staff_organization_id                                  as staff_organization_id
        ,data_table.agent_number                                            as agent_number
        ,data_table.store_number                                            as store_number
        ,data_table.record_wtd_number                                       as record_wtd_number
        ,data_table.record_mtd_number                                       as record_mtd_number
        ,data_table.guide_wtd_number                                        as guide_wtd_number
        ,data_table.guide_mtd_number                                        as guide_mtd_number
        ,data_table.deal_wtd_number                                         as deal_wtd_number
        ,data_table.deal_mtd_number                                         as deal_mtd_number
        ,'${wf:id()}'      as load_job_number
        ,'${wf:name()}'    as load_job_name
        ,current_timestamp as insert_timestamp
        ,2 as source_system_code
  from(
        select
                business_staff_id          as staff_id
               ,business_staff_org_id      as organization_id
               ,business_staff_sf_org_id   as staff_organization_id
          from edw_public.dim_edw_pub_business_staff_base_info
         where dt='${dt}'
           and is_delete_flag='N'
           and business_staff_role_id=1
           and real_staff=1
      )staff_table
    join(
        select
                 total_table.agent_company_id                                       as company_id
                ,total_table.staff_id                                               as staff_id
                ,count(distinct total_table.agent_id)                              as agent_number
                ,count(distinct total_table.agent_store_id)                        as store_number
                ,sum(total_table.agent_record_wtd_count)                            as record_wtd_number
                ,sum(total_table.agent_record_mtd_count)                            as record_mtd_number
                ,sum(total_table.agent_guide_wtd_count)                             as guide_wtd_number
                ,sum(total_table.agent_guide_mtd_count)                             as guide_mtd_number
                ,sum(total_table.agent_deal_wtd_count)                              as deal_wtd_number
                ,sum(total_table.agent_deal_mtd_count)                              as deal_mtd_number
          from(
                select
                        a.agent_id                   as agent_id
                       ,a.agent_store_id             as agent_store_id
                       ,a.agent_company_id           as agent_company_id
                       ,c.staff_id                   as staff_id
                       ,c.organization_id            as organization_id
                       ,c.staff_organization_id      as staff_organization_id
                       ,a.agent_record_wtd_count     as agent_record_wtd_count
                       ,a.agent_record_mtd_count     as agent_record_mtd_count
                       ,a.agent_guide_wtd_count      as agent_guide_wtd_count
                       ,a.agent_guide_mtd_count      as agent_guide_mtd_count
                       ,a.agent_deal_wtd_count       as agent_deal_wtd_count
                       ,a.agent_deal_mtd_count       as agent_deal_mtd_count
                  from(
                        select
                                coalesce(a1.agent_id,a2.agent_id)                  as agent_id
                               ,coalesce(a1.agent_store_id,a2.agent_store_id)      as agent_store_id
                               ,coalesce(a1.agent_company_id,a2.agent_company_id)  as agent_company_id
                               ,coalesce(a1.agent_record_wtd_count,0)              as agent_record_wtd_count
                               ,coalesce(a1.agent_record_mtd_count,0)              as agent_record_mtd_count
                               ,coalesce(a1.agent_guide_wtd_count,0)               as agent_guide_wtd_count
                               ,coalesce(a1.agent_guide_mtd_count,0)               as agent_guide_mtd_count
                               ,coalesce(a2.agent_deal_wtd_count,0)                as agent_deal_wtd_count
                               ,coalesce(a2.agent_deal_mtd_count,0)                as agent_deal_mtd_count
                          from(
                                select
                                        agent_id
                                       ,agent_store_id
                                       ,agent_company_id
                                       ,agent_record_wtd_count
                                       ,agent_record_mtd_count
                                       ,agent_guide_wtd_count
                                       ,agent_guide_mtd_count
                                  from edw_agents.adm_edw_agent_all_business_001_di
                                 where dt='${dt}'
                                   and source_system_code=2
                            )a1
                           full join(
                                select
                                        agent_id
                                       ,agent_deal_wtd_count
                                       ,agent_deal_mtd_count
                                       ,agent_store_id
                                       ,agent_company_id
                                  from edw_agents.adm_edw_agent_all_business_002_di
                                 where dt='${dt}'
                                   and source_system_code=2
                            )a2
                            on a1.agent_id=a2.agent_id and a1.agent_store_id=a2.agent_store_id and a1.agent_company_id=a2.agent_company_id
                    )a
                  join(
                        select
                                agent_store_id
                               ,agent_store_xf_business_staff_id   as staff_id
                          from edw_public.dim_edw_pub_agent_store_base_info
                         where dt='${dt}'
                           and agent_store_deleted_flag=0
                           and agent_store_virtual_flag='N'
                     )b
                  on a.agent_store_id=b.agent_store_id
                  join(
                        select
                                 business_staff_id          as staff_id
                                ,business_staff_org_id      as organization_id
                                ,business_staff_sf_org_id   as staff_organization_id
                          from edw_public.dim_edw_pub_business_staff_base_info
                         where dt='${dt}'
                           and is_delete_flag='N'
                           and business_staff_role_id=1
                           and real_staff=1
                     )c
                  on b.staff_id=c.staff_id
             )total_table
          group by total_table.agent_company_id,total_table.staff_id
   )data_table
  on staff_table.staff_id=data_table.staff_id
;