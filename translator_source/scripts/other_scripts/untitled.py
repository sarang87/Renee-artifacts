import random

def generate_rand(len_rand):
    s=""
    for i in range(len_rand):
        s+=random.randint(0,1)
    return s

fnc_inst_cnt_dict = {'PeeredDispatcher_EventPairDispatcher___get_lock__const': 3, 'fbl__RefPtr_ThreadDispatcher_DownCastDispatcher_ThreadDispatcher__fbl__RefPtr_Dispatcher': 21, 'PeeredDispatcher_EventPairDispatcher___get_related_koid__const': 2, 'DummyIommu__Unmap_unsignedlong_unsignedlong_unsignedlong': 5, 'gicv2_read_gich_lr_unsignedint': 7, 'write_cntp_cval': 3, 'arm64_get_cache_info': 76, 'GuestDispatcher__get_type__const': 2, 'VmObjectPaged__is_contiguous__const': 3, '_anonymousnamespace___PciMmioConfig__Write_PciReg16_unsignedshort_const': 5, 'isspace': 8, 'BusTransactionInitiatorDispatcher__has_state_tracker__const': 2, 'VmObjectPhysical__size__const': 2, 'gic_write_gich_lr_unsignedint_unsignedlong': 4, 'wait_queue_blocked_priority': 11, 'el2_hvc_psci': 2, 'arm64_el2_on': 2, 'gicv2_get_lr_from_vector_unsignedint': 3, 'uart_puts': 4, 'FutexNode__FutexNode': 9, 'fbl__RefPtr_ResourceDispatcher_DownCastDispatcher_ResourceDispatcher__fbl__RefPtr_Dispatcher': 21, 'ProfileDispatcher__has_state_tracker__const': 2, 'VmObject__CleanCache_unsignedlong_unsignedlong': 2, 'mp_set_curr_cpu_online': 28, 'qrcodegen__QrCode__QrCode': 6, 'gfx_fillrect': 20, 'EventDispatcher__has_state_tracker__const': 2, 'imx_uart_pputc': 11, 'fbl__RefPtr_ProcessDispatcher_DownCastDispatcher_ProcessDispatcher__fbl__RefPtr_Dispatcher': 21, 'DummyIommu__IsValidBusTxnId_unsignedlong_const': 2, 'fbl__AllocChecker__AllocChecker': 2, 'PeeredDispatcher_FifoDispatcher___get_lock__const': 3, 'VmObject__Resize_unsignedlong': 2, 'PcieBridge__mmio_lo_regions': 2, '_vsnprintf_output': 17, 'memset': 97, 'PcieBridge__mmio_hi_regions': 2, 'VmObject__size__const': 2, 'operatornew_unsignedlong_void': 2, 'Pci__PioCfgRead_unsignedint_unsignedint__unsignedlong': 2, 'gic_read_gich_vmcr': 4, 'parse_ccsid_arm64_cache_desc_t__unsignedlong': 19, 'arm64_init_percpu_early': 11, 'od.crypto__entropy._anonymousnamespace___MockCollector___MockCollector': 6, 'arm64_el2_gicv3_read_gich_misr': 4, 'VmAddressRegionDummy__CreateSubVmar_unsignedlong_unsignedlong_unsignedchar_unsignedint_charconst__fbl__RefPtr_VmAddressRegion': 2, 'gicv2_default_gich_vmcr': 2, 'sys_syscall_test_6_int_int_int_int_int_int': 6, 'ARGB8888_to_RGB332': 8, 'arm64_get_secondary_sp': 17, 'platform_mp_cpu_hotplug': 3, 'gicv2_read_gich_vtr': 4, 'thread_init_early': 43, 'VmAddressRegionDummy__DestroyLocked': 2, 'boot_alloc_page_phys': 7, 'arm_smccc_hvc': 6, 'hisi_reboot': 16, 'PcieBusDriver__PcieBusDriver_PciePlatformInterface': 130, 'VmAddressRegionDispatcher__get_type__const': 2, 'EventDispatcher__get_type__const': 2, 'write_cntv_tval': 4, 'fbl__RefPtr_SocketDispatcher_DownCastDispatcher_SocketDispatcher__fbl__RefPtr_Dispatcher': 21, 'PcieRoot__pio_regions': 3, 'gicv2_write_gich_hcr_unsignedint': 4, 'default_handle_fiq': 1, 'EventPairDispatcher__get_type__const': 2, 'MBufChain__is_empty__const': 4, 'PortDispatcher__get_type__const': 2, 'Dispatcher__Dispatcher_unsignedint': 37, 'gic_send_ipi': 19, 'imx_uart_pgetc': 11, 'display_get_info': 2, 'hisi_power_init': 64, 'isalpha': 5, 'LogDispatcher__has_state_tracker__const': 2, 'VmAddressRegion__is_mapping__const': 2, 'psci_hvc_call': 11, 'arm_gicv2m_get_frame_info': 52, 'el2_hvc_sysreg': 4, 'gicv2_read_gich_elrsr': 4, 'copyrect8': 53, 'VmAddressRegionOrMapping__as_vm_mapping': 88, 'FutexContext__FutexContext': 16, 'gic_shutdown_1': 6, 'pl011_start_panic': 3, 'putpixel8': 14, 'arm64_el2_resume': 2, 'MBufChain__is_full__const': 6, 'write_cntps_ctl': 4, 'FifoDispatcher__has_state_tracker__const': 2, 'el2_hvc_mexec': 1, 'arm64_el2_off': 2, 'platform_irq': 4, 'VmObject__InvalidateCache_unsignedlong_unsignedlong': 2, 'bitmap__RawBitmapGeneric_bitmap__FixedStorage_8ul_____RawBitmapGeneric': 1, 'fbl__RefPtr_LogDispatcher_DownCastDispatcher_LogDispatcher__fbl__RefPtr_Dispatcher': 21, 'platform_early_console_enabled': 2, 'timer_init': 11, 'strlen': 10, 'cmpct_test': 1, 'VmObject__CommitRange_unsignedlong_unsignedlong_unsignedlong': 2, 'gicv3_get_vector_from_lr_unsignedlong': 1, 'default_configure': 2, 'crypto__entropy__EarlyBootTest': 1, 'arch_thread_initialize': 23, 'gic_get_interrupt_config': 12, 'cntpct_to_zx_time': 5, 'bitmap__Bitmap__ClearOne_unsignedlong': 4, 'default_is_valid': 2, 'sys_mmap_device_io_unsignedint_unsignedint_unsignedint': 2, 'PortObserver__OnCancelByKey_Handleconst__voidconst__unsignedlong': 16, 'mtrace_control_unsignedint_unsignedint_unsignedint_internal__user_ptr_void__internal__InOutPolicy_3__unsignedlong': 2, 'hypervisor__percpu_task_void': 20, 'page_state_to_string_unsignedint': 33, 'fbl__RefPtr_ChannelDispatcher_DownCastDispatcher_ChannelDispatcher__fbl__RefPtr_Dispatcher': 21, 'non_virtualthunktoPcieBridge__pio_regions': 2, 'power_reboot': 4, 'PeeredDispatcher_SocketDispatcher___get_lock__const': 3, 'SocketDispatcher__get_type__const': 2, 'ArmArchVmAspace__arch_table_phys__const': 2, '_anonymousnamespace___validate_thread_state_input_unsignedint_unsignedlong_unsignedlong___clone.constprop.64': 41, 'gic_get_vector_from_lr_unsignedlong': 4, 'remove_queue_head_thread': 33, 'crypto__PRNG__is_thread_safe__const': 6, 'removal__RmOnStateChange__OnStateChange_unsignedint': 2, 'fbl__RefPtr_TimerDispatcher_DownCastDispatcher_TimerDispatcher__fbl__RefPtr_Dispatcher': 21, 'arch_clean_invalidate_cache_range': 11, 'FutexNode__AppendList_FutexNode': 7, 'PortDispatcher__DefaultPortAllocator': 3, 'platform_mexec_void____unsignedlong_unsignedlong_unsignedlong_unsignedlong_memmov_ops_t__void___memmov_ops_t__unsignedlong_unsignedlong_unsignedlong': 61, 'counters_init_unsignedint': 20, 'removal__RemovableObserver__OnRemoved': 4, 'TimerDispatcher__has_state_tracker__const': 2, 'DummyIommu__ClearMappingsForBusTxnId_unsignedlong': 2, 'boot_alloc_init': 7, 'interrupt_init_percpu_early': 4, 'mandatory_memset': 8, 'arm_gic_v2_init': 274, 'PciCapPcie___PciCapPcie': 10, 'PcieDevice__DoFunctionLevelReset_____lambda_void___4____FUN_void': 8, 'gicv2_get_vector_from_lr_unsignedlong': 2, 'arm64_get_kernel_ptable': 3, 'fbl__RefPtr_JobDispatcher_DownCastDispatcher_JobDispatcher__fbl__RefPtr_Dispatcher': 21, 'pdev_register_interrupts': 4, 'hexval': 19, 'mp_sync_task_void': 21, 'arm64_get_boot_el': 4, 'VmObject__ResizeLocked_unsignedlong': 2, 'putpixel16': 15, 'TimerDispatcher__get_type__const': 2, 'arch_spin_lock': 9, 'StateObserver__OnRemoved': 1, 'write_cntp_tval': 4, 'alloc_checker_panic': 2, 'platform_mp_cpu_unplug': 1, 'mexec_arch_clean_invalidate_cache_all': 38, 'crashlog_print_callback___print_callback__charconst__unsignedlong': 20, 'ProcessDispatcher__get_related_koid__const': 3, 'f__geterrno': 3, 'mymemcpy_void__voidconst__unsignedlong': 1, 'PcieBridge__pf_mmio_regions': 2, 'VmObject__SyncCache_unsignedlong_unsignedlong': 2, 'cbuf_space_avail': 11, 'qrcodegen__QrCode__getNumDataCodewords_int_qrcodegen__Eccconst': 36, 's905_uart_pputc': 11, 'get_paddr_void__unsignedlong_unsignedlong_unsignedlong': 3, 'VmObjectPaged__is_resizable__const': 3, 'default_pgetc': 2, 'Dispatcher__get_related_koid__const': 2, 'gicv3_get_gicv_unsignedlong': 2, 'write_cntv_ctl': 4, 'VmEnumerator__OnVmMapping_VmMappingconst__VmAddressRegionconst__unsignedint': 2, 'ResourceDispatcher__get_cookie_jar': 2, 'ProfileDispatcher__get_type__const': 2, 'LogDispatcher__get_type__const': 2, 'VmObject__GetPageLocked_unsignedlong_unsignedint_list_node__vm_page___unsignedlong': 2, 'PcieRootLUTSwizzle__Swizzle_unsignedint_unsignedint_unsignedint_unsignedint': 21, 'PmmArena__CountStates_unsignedlong__const': 19, 'VmAddressRegionDummy__EnumerateChildrenLocked_VmEnumerator__unsignedint': 2, 'remap_interrupt': 4, 'target_early_init': 1, 'SoloDispatcher__get_lock__const': 2, 'isupper': 4, 'DummyIommu__aspace_size_unsignedlong': 2, 'hypervisor__cpu_of_unsignedshort': 7, 's905_uart_start_panic': 3, 'rand': 15, 'gfx_putpixel.part.0': 2, 'arm64_el2_gicv3_read_gich_elrsr': 4, 'arm64_exc_shared_restore_short': 17, 'platform_fiq': 4, 'gic_shutdown': 6, 'boot_reserve_range_search_unsignedlong_unsignedlong_unsignedlong_reserve_range_t': 37, 'VmObjectDispatcher__has_state_tracker__const': 2, 'udisplay_set_display_info': 11, 'VmObjectPaged__size__const': 2, 'bitmap__RawBitmapBase__Set_unsignedlong_unsignedlong': 40, 'periph_paddr_to_vaddr': 19, 'gic_read_gich_hcr': 4, 'ARGB8888_to_RGB2220': 9, 'EventPairDispatcher__allowed_user_signals__const': 3, 'sys_syscall_test_7_int_int_int_int_int_int_int': 7, 'gic_write_gich_hcr_unsignedint': 4, 'VmObject__is_contiguous__const': 2, 'bitmap__Bitmap__SetOne_unsignedlong': 4, 'arm64_el2_gicv3_write_gich_lr': 4, 'gic_mask_interrupt': 20, 'ResourceDispatcher__has_state_tracker__const': 2, 'JobDispatcher__get_type__const': 2, 'Dispatcher__get_name_char__const': 4, 'SocketDispatcher__has_state_tracker__const': 2, 'SHA256_Init': 31, 'clSHA256': 42, 'qrcodegen__QrCode__drawAlignmentPattern_int_int': 36, 'arm64_exc_shared_restore_long': 24, 'uart_pputc': 4, 'hypervisor__check_pinned_cpu_invariant_unsignedshort_threadconst': 24, 'gicv3_get_lr_from_vector_unsignedint': 4, 'psci_system_reset': 31, 'mutex_init': 9, 'PortObserver__OnCancel_Handleconst': 5, 'default_shutdown_1': 1, 'VmObjectDispatcher__get_type__const': 2, 'Semaphore__Semaphore_long': 8, 'PciStdCapability___PciStdCapability': 10, 'InterruptDispatcher__get_type__const': 2, 'bitmap__RawBitmapBase__Clear_unsignedlong_unsignedlong': 40, 'tolower': 5, 'sys_syscall_test_5_int_int_int_int_int': 5, 'ArmArchVmAspace__ArmArchVmAspace': 20, 'VmPageList__IsEmpty': 4, 'removal__on_cancel____RmOnCancel__OnCancel_Handleconst': 2, 'arch_clean_cache_range': 11, 'gic_init_percpu_early': 10, 'arch_invalidate_cache_range': 11, 'memmove_mexec': 19, 'strncasecmp': 45, 'VcpuDispatcher__get_type__const': 2, 'arm64_el2_gicv3_read_gich_vtr': 4, 'bitmap__RawBitmapGeneric_bitmap__FixedStorage_65535ul_____RawBitmapGeneric': 1, 'EventDispatcher__allowed_user_signals__const': 3, 'gfxconsole_putpixel': 14, 'PeeredDispatcher_ChannelDispatcher___get_lock__const': 3, 'arch_set_fp_regs': 2, 'clSHA256_init': 22, 'gicv3_get_num_lrs': 7, 'VmObject__SetMappingCachePolicy_unsignedint': 2, 'arm64_el2_tlbi_ipa': 3, 'gic_get_gicv_unsignedlong': 4, 'GetSystemPolicyManager': 3, 'copyrect16': 57, 'fbl__RefPtr_InterruptDispatcher_DownCastDispatcher_InterruptDispatcher__fbl__RefPtr_Dispatcher': 21, 'ThreadDispatcher__has_state_tracker__const': 2, 'default_init_percpu': 1, 'gic_get_interrupt_config_1': 12, 'PcieDevice__DoFunctionLevelReset_____lambda_void___2____FUN_void': 21, 'gicv2_read_gich_hcr': 4, 'fbl__RefPtr_VmObjectDispatcher_DownCastDispatcher_VmObjectDispatcher__fbl__RefPtr_Dispatcher': 21, 'vmo_lookup_test_____lambda_void__unsignedlong_unsignedlong_unsignedlong__1____FUN_void__unsignedlong_unsignedlong_unsignedlong': 6, 'arm64_el2_gicv3_read_gich_hcr': 4, 'crash_thread_void': 4, 'bitmap__RawBitmapBase__ClearAll': 11, 'read_cntpct': 2, 'gic_read_gich_lr_unsignedint': 4, 'mp_set_curr_cpu_active': 29, 'ticks_per_second': 16, 'hw_rng_get_entropy': 2, 'arm64_uspace_entry': 35, 'gic_remap_interrupt': 1, 'PeeredDispatcher_FifoDispatcher___get_related_koid__const': 2, 'PeeredDispatcher_ChannelDispatcher___get_related_koid__const': 2, 'arch_get_fp_regs': 2, 'y1.init': 35, 'default_handle_irq': 1, 'mymemset_void__int_unsignedlong': 1, 'PinnedMemoryTokenDispatcher__get_type__const': 2, 'strchr': 11, 'VmObject__DecommitRange_unsignedlong_unsignedlong_unsignedlong': 2, 'removal__on_initialize____RmOnInitialize__OnInitialize_unsignedint_StateObserver__CountInfoconst': 2, 'VmObject__AllocatedPagesInRange_unsignedlong_unsignedlong_const': 2, 'VmObjectPhysical__is_contiguous__const': 2, 'arch_thread_construct_first': 10, 'PcieRoot__PcieRoot_PcieBusDriver__unsignedint': 26, 'sys_syscall_test_0': 2, 'el2_hvc_resume': 145, 'fbl__RefPtr_FifoDispatcher_DownCastDispatcher_FifoDispatcher__fbl__RefPtr_Dispatcher': 21, 'VmObject__Pin_unsignedlong_unsignedlong': 2, 'default_remap': 2, 'arm64_el2_gicv3_write_gich_hcr': 4, 'VmEnumerator__OnVmAddressRegion_VmAddressRegionconst__unsignedint': 2, 'VmObject__ReadUser_internal__user_ptr_void__internal__InOutPolicy_2__unsignedlong_unsignedlong': 2, 'gic_configure_interrupt': 30, 'gic_read_gich_elrsr': 4, 'DummyIommu__Map_unsignedlong_fbl__RefPtr_VmObject_const__unsignedlong_unsignedlong_unsignedint_unsignedlong__unsignedlong_____lambda_void__unsignedlong_unsignedlong_unsignedlong__1____FUN_void__unsignedlong_unsignedlong_unsignedlong': 3, 'el2_gicv3_read_lr': 3, 'PcieDevice__DoFunctionLevelReset_____lambda_void___3____FUN_void': 12, 'VmPageList__VmPageList': 4, 'VmAddressRegionDummy__FindRegion_unsignedlong': 3, 'arch_mp_prep_cpu_unplug': 2, 'gic_unmask_interrupt': 20, 'sys_pci_cfg_pio_rw_unsignedint_unsignedchar_unsignedchar_unsignedchar_unsignedchar_internal__user_ptr_unsignedint__internal__InOutPolicy_3__unsignedlong_bool': 2, 'EventPairDispatcher__get_cookie_jar': 2, 'ChannelDispatcher__has_state_tracker__const': 2, 'arm64_el2_gicv3_read_gich_vmcr': 4, 'Dispatcher__has_state_tracker__const': 2, '_anonymousnamespace___TestDispatcher__has_state_tracker__const': 2, 'mmu_flags_to_s1_pte_attr_unsignedint': 36, 'fbl__RefPtr_VcpuDispatcher_DownCastDispatcher_VcpuDispatcher__fbl__RefPtr_Dispatcher': 21, 'PcieBridge__pio_regions': 2, 'arch_smc_call_zx_smc_parametersconst__zx_smc_result': 21, 'draw_char': 64, 'ResourceDispatcher__get_type__const': 2, 'StateObserver__OnCancelByKey_Handleconst__voidconst__unsignedlong': 2, 'gic_default_gich_vmcr': 4, 'target_init': 1, 'arm64_fpu_context_switch': 30, '_HASH_final': 73, 'VmObject__CloneCOW_bool_unsignedlong_unsignedlong_bool_fbl__RefPtr_VmObject': 2, 'el2_gicv3_done': 3, 'gic_is_valid_interrupt': 5, 'is_valid_interrupt': 4, 'VmObject__Lookup_unsignedlong_unsignedlong_unsignedint_int____void__unsignedlong_unsignedlong_unsignedlong__void': 2, '_anonymousnamespace___PciMmioConfig__Write_PciReg32_unsignedint_const': 4, '_anonymousnamespace___PciMmioConfig__Read_PciReg32_const': 4, 'gicv3_read_gich_elrsr': 6, '_HASH_update': 33, 'PcieDevice__PcieDevice_PcieBusDriver__unsignedint_unsignedint_unsignedint_bool': 45, 'arch_prepare_current_cpu_idle_state': 1, 'VirtualInterruptDispatcher__UnmaskInterrupt': 1, 'EventDispatcher__get_cookie_jar': 2, 'Dispatcher__set_name_charconst__unsignedlong': 2, 'ThreadDispatcher__get_type__const': 2, 'write_cntv_cval': 3, 'event_init': 11, 'mask_interrupt': 4, 'Dispatcher__allowed_user_signals__const': 2, 'removal__on_cancel_by_key____RmOnCancelByKey__OnCancelByKey_Handleconst__voidconst__unsignedlong': 2, 'fbl__RefPtr_VmAddressRegionDispatcher_DownCastDispatcher_VmAddressRegionDispatcher__fbl__RefPtr_Dispatcher': 21, 'fbl__AllocChecker__check': 5, 'arch_mp_cpu_unplug': 2, 'Dispatcher__on_zero_handles': 1, 'isdigit': 4, 'bitmap__Bitmap__GetOne_unsignedlong_const': 5, 'PcieRoot__mmio_hi_regions': 3, 'current_time': 38, 'configure_interrupt': 4, 'VmAddressRegionDummy__Protect_unsignedlong_unsignedlong_unsignedint': 2, 'platform_mp_prep_cpu_unplug': 1, 'VmObjectDispatcher__get_cookie_jar': 2, 'JobDispatcher__get_related_koid__const': 6, 'imx_start_panic': 3, 'hexdump8_very_ex': 82, 'write_cntps_tval': 4, 'hypervisor__BlockingPortAllocator__BlockingPortAllocator': 29, 'mp_prepare_current_cpu_idle_state': 1, 'default_start_panic': 1, 'ARGB8888_to_Luma': 11, 'fbl__RefPtr_PcieUpstreamNode____RefPtr': 23, 'JobEnumerator__OnJob_JobDispatcher': 2, 'arch_mp_init_percpu': 5, 'PinnedMemoryTokenDispatcher__has_state_tracker__const': 2, 'removal__RemovableObserver__OnStateChange_unsignedint': 2, 'VmObject__CleanInvalidateCache_unsignedlong_unsignedlong': 2, 'default_mask': 2, 'putpixel32': 5, 'sys_syscall_test_4_int_int_int_int': 4, 'pci_class_code_to_string_unsignedchar': 103, 'non_virtualthunktoPcieBridge__mmio_lo_regions': 2, 'ProcessDispatcher__get_type__const': 2, 'VmAddressRegionDummy__Activate': 1, 'uart_pgetc': 4, 'pl011_uart_pputc': 9, 'gicv2_write_gich_vmcr_unsignedint': 4, 'sys_syscall_test_1_int': 1, 'sys_syscall_test_3_int_int_int': 3, 'rol64': 9, 'gicv2_read_gich_vmcr': 4, 'IommuDispatcher__get_type__const': 2, 'sys_syscall_test_2_int_int': 2, 'gic_get_lr_from_vector_unsignedint': 4, 'VmObject__Write_voidconst__unsignedlong_unsignedlong': 2, 'removal__RemovableObserver__OnCancelByKey_Handleconst__voidconst__unsignedlong': 2, 'gic_init_percpu': 23, 'VmAspace__vaddr_to_aspace_unsignedlong': 17, 'PmmNode__CountTotalBytes__const': 2, 'pl011_uart_pgetc': 8, '_anonymousnamespace___PciMmioConfig__Write_PciReg8_unsignedchar_const': 5, 'PcieDevice__DoFunctionLevelReset_____lambda_void___1____FUN_void': 12, 'JobDispatcher__has_state_tracker__const': 2, 'uart_getc': 4, 'arch_invalidate_cache_all': 36, 'VmAddressRegionDummy__AllocatedPages__const': 2, 'PcieRoot__pf_mmio_regions': 3, 'cmd_echo': 7, 'psci_system_off': 9, 'null_memcpy_void__voidconst__unsignedlong': 1, 'FifoDispatcher__get_type__const': 2, 'gicv2_read_gich_misr': 4, 'fbl__RefPtr_BusTransactionInitiatorDispatcher_DownCastDispatcher_BusTransactionInitiatorDispatcher__fbl__RefPtr_Dispatcher': 21, 'jent_have_clock': 2, 'pmm_count_total_bytes': 3, 'strcmp': 13, 'gfx_copyrect': 30, 'removal__RemovableObserver__OnInitialize_unsignedint_StateObserver__CountInfoconst': 2, 'timer_queue_init': 10, 'Pci__PioCfgWrite_unsignedint_unsignedint_unsignedlong': 2, 'VmObject__GetMappingCachePolicy_unsignedint': 2, 'gicv2_write_gich_lr_unsignedint_unsignedlong': 6, 'VDso__base_address_fbl__RefPtr_VmMapping_const': 7, 'arch_enter_uspace': 15, 'VmObject__LookupUser_unsignedlong_unsignedlong_internal__user_ptr_unsignedlong__internal__InOutPolicy_3__unsignedlong': 2, 'psci_smc_call': 11, 'shutdown_interrupts': 4, 'gic_remap_interrupt_1': 1, 'isxdigit': 10, 'Dispatcher__get_cookie_jar': 2, 'VmObject__is_paged__const': 2, 'hypervisor__guest_lookup_page_void__unsignedlong_unsignedlong_unsignedlong': 3, 'ARGB8888_to_RGB565': 8, 'sys_syscall_test_8_int_int_int_int_int_int_int_int': 8, 'arm64_el2_tlbi_vmid': 3, 'PcieRoot__mmio_lo_regions': 3, 'platform_get_ramdisk': 9, '_anonymousnamespace___PciMmioConfig__Read_PciReg16_const': 4, 'zbi_for_each': 51, 'DummyIommu__minimum_contiguity_unsignedlong': 2, 'fbl__RefPtr_PortDispatcher_DownCastDispatcher_PortDispatcher__fbl__RefPtr_Dispatcher': 21, 'sys_syscall_test_wrapper_int_int_int': 3, 'default_get_config': 2, 'wait_queue_remove_thread_thread': 10, 'VmObject__Read_void__unsignedlong_unsignedlong': 2, 'arm64_el2_gicv3_write_gich_vmcr': 4, 'write_cntps_cval': 3, 'non_virtualthunktoPcieBridge__mmio_hi_regions': 2, 'VmAddressRegionDummy__Destroy': 2, 'arch_sync_cache_range': 22, 'ProcessDispatcher__has_state_tracker__const': 2, 's905_uart_pgetc': 10, 'isprint': 4, 'sched_resched_internal': 297, 'PciDeviceDispatcher__get_type__const': 2, 's905_uart_init': 146, 'ChannelDispatcher__get_type__const': 2, 'arch_spin_trylock': 7, '_anonymousnamespace___TestDispatcher__get_type__const': 2, 'el2_gicv3_write_lr': 3, 'wait_queue_init': 6, 'fbl__RefPtr_GuestDispatcher_DownCastDispatcher_GuestDispatcher__fbl__RefPtr_Dispatcher': 21, 'BusTransactionInitiatorDispatcher__get_type__const': 2, 'VmMapping__is_mapping__const': 2, 'uart_irq': 61, 'EventPairDispatcher__has_state_tracker__const': 2, 'mp_init': 17, 'VmObject__is_resizable__const': 2, 'VmObjectPaged__is_paged__const': 2, 'PeeredDispatcher_SocketDispatcher___get_related_koid__const': 2, 'record_recv_msg_sz_unsignedint': 121, 'mp_mbx_interrupt_irq': 2, 'jent_fips_enabled': 2, 'default_send_ipi': 2, 'removal__RemovableObserver__OnCancel_Handleconst': 2, 'write_cntp_ctl': 4, 'platform_stop_timer': 5, 'non_virtualthunktoPcieBridge__pf_mmio_regions': 2, 'PciCapMsi___PciCapMsi': 10, 'VmAddressRegionDummy__Unmap_unsignedlong_unsignedlong': 2, 'gic_write_gich_vmcr_unsignedint': 4, 'VmAddressRegionDispatcher__is_valid_mapping_protection_unsignedint': 6, 'read_cntvct': 2, 'VmObject__WriteUser_internal__user_ptr_voidconst__internal__InOutPolicy_1__unsignedlong_unsignedlong': 2, 'gic_read_gich_misr': 4, 'gic_get_num_lrs': 4, 'fbl__RefPtr_PciDeviceDispatcher_DownCastDispatcher_PciDeviceDispatcher__fbl__RefPtr_Dispatcher': 21, 'power_shutdown': 4, 'arch_zero_page': 9, 'copyrect32': 57, 'arch_thread_get_blocked_fp': 3, 'VmAddressRegionDummy__AllocatedPagesLocked__const': 2, 'ExceptionPort__BuildArchReport_zx_exception_report__unsignedint_arch_exception_contextconst': 27, 'arm64_el2_gicv3_read_gich_lr': 5, 'PmmNode__PmmNode': 28, 'PmmNode__CountFreePages__const': 2, 'crypto__entropy__HwRngCollector__GetInstance_crypto__entropy__Collector': 3, 'current_ticks': 4, 'default_pputc': 2, 'gicv2_get_num_lrs': 6, 'arm_generic_timer_resume_cpu': 14, 'default_getc': 2, 'arch_system_powerctl_unsignedint_zx_system_powerctl_argconst': 2, 'ChannelDispatcher__TxMessageMax__const': 2, 'default_init_percpu_early': 1, 'arch_mp_send_ipi': 23, 'gic_configure_interrupt_1': 30, 'VmAddressRegionDummy__Dump_unsignedint_bool_const': 1, 'gicv3_default_gich_vmcr': 3, 'zbi_create_section': 80, 'default_dputs': 1}

ret_str1 = "1101011001011111000000" 
ret_str2 = generate_rand(5)
ret_str3 = "00000"
ret_str = ret_str1 + ret_str2 + ret_str3
print ret_str
output_file = open ("ret_test.pvs", "w")
output_file.write("ret_      : THEORY")
output_file.write("\tBEGIN")
output_file.write("\tIMPORTING rsl@arm_state, rsl@ret\n")    
#output_file.write("\t\tX_sts : [ below(32) -> bvec[64] ]  = init`X")
#output_file.write("\t\tp    :  s = init with  [ `X(–):= bv[64](0b )  ]
#output_file.write("\t\tret_1 : Theory = ret [ p ] {{ Diag:= (bv[32](0b  — )) }} % Diag is generated from ret diagram.\n")    
# % reverse this as usual in python, it seems like the last version was not reversed.")
output_file.write("\ttest1 : lemma  ret_1.post`PC`b = bv[64](0b —) % this is the same as `X() above." )  
output_file.write("%|- p_TCC1         : PROOF")
output_file.write("%|- ret_1_TCC*     : PROOF")
output_file.write("%|- test1_TCC1     : PROOF (eval-formula)")
output_file.write("%|- QED")
output_file.write("%|- test1 : PROOF ( ret )")
output_file.write("%|- QED")

#if __name__== "__main__":
#  main()