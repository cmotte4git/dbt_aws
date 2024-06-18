with source as (
      select * from  public.fct_dvf_full WHERE date_mutation > '2023-11-04'
),
dvf_full as (
    select
        *

    from source
)
select * from dvf_full
  
  