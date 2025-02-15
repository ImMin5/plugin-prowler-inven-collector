from typing import List
from cloudforet.plugin.model.cloud_service_type_model import BaseCloudServiceType

_METADATA = {
    'query_sets': [
        {
            'name': 'AWS Prowler',
            'unit': {
                'pass_score': '%',
                'fail_score': '%'
            },
            'query_options': {
                'group_by': [
                    'data.status',
                    'data.severity',
                    'data.service'
                ],
                'fields': {
                    'compliance_count': {
                        'operator': 'count'
                    },
                    'fail_check_count': {
                        'key': 'data.stats.checks.fail',
                        'operator': 'sum'
                    },
                    'pass_check_count': {
                        'key': 'data.stats.checks.pass',
                        'operator': 'sum'
                    },
                    'info_check_count': {
                        'key': 'data.stats.checks.info',
                        'operator': 'sum'
                    },
                    'fail_finding_count': {
                        'key': 'data.stats.findings.fail',
                        'operator': 'sum'
                    },
                    'pass_finding_count': {
                        'key': 'data.stats.findings.pass',
                        'operator': 'sum'
                    },
                    'info_finding_count': {
                        'key': 'data.stats.findings.info',
                        'operator': 'sum'
                    },
                    'fail_score': {
                        'key': 'data.stats.score.fail',
                        'operator': 'sum'
                    },
                    'pass_score': {
                        'key': 'data.stats.score.pass',
                        'operator': 'sum'
                    }
                }
            }
        }
    ],
    'view': {
        'search': [
            {
                'key': 'data.requirement_id',
                'name': 'Requirement ID'
            },
            {
                'key': 'data.status',
                'name': 'Status',
                'enums': [
                    'FAIL',
                    'PASS',
                    'INFO'
                ]
            },
            {
                'key': 'data.stats.score.percent',
                'name': 'Compliance Score',
                'data_type': 'float'
            },
            {
                'key': 'data.severity',
                'name': 'Severity',
                'enums': [
                    'CRITICAL',
                    'HIGH',
                    'MEDIUM',
                    'LOW',
                    'INFORMATIONAL'
                ]
            },
            {
                'key': 'data.service',
                'name': 'Service'
            }
        ],
        'table': {
            'layout': {
                'name': '',
                'type': 'query-search-table',
                'options': {
                    'default_sort': {
                        'key': 'data.requirement_id',
                        'desc': False
                    },
                    'fields': [
                        {
                            'type': 'text',
                            'key': 'data.requirement_id',
                            'name': 'Requirement ID'
                        },
                        {
                            'type': 'text',
                            'key': 'data.description',
                            'name': 'Description',
                            'options': {
                                'is_optional': True
                            }
                        },
                        {
                            'type': 'enum',
                            'name': 'Status',
                            'key': 'data.status',
                            'options': {
                                'FAIL': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'coral.500'
                                    }
                                },
                                'PASS': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'indigo.500'
                                    }
                                },
                                'INFO': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'peacock.500'
                                    }
                                }
                            }
                        },
                        {
                            'type': 'text',
                            'key': 'data.display.findings',
                            'name': 'Findings',
                            'options': {
                                'sortable': False
                            }
                        },
                        {
                            'type': 'text',
                            'key': 'data.display.checks',
                            'name': 'Checks',
                            'options': {
                                'sortable': False,
                                'is_optional': True
                            }
                        },
                        {
                            'type': 'text',
                            'key': 'data.stats.score.percent',
                            'name': 'Compliance Score',
                            'options': {
                                'is_optional': True
                            }
                        },
                        {
                            'type': 'text',
                            'key': 'data.severity',
                            'name': 'Severity'
                        },
                        {
                            'type': 'text',
                            'key': 'data.service',
                            'name': 'Service'
                        }
                    ]
                }
            }
        },
        'widget': [
            {
                'name': 'Total Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': []
                }
            },
            {
                'name': 'Failed Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.status', 'value': 'FAIL', 'operator': 'eq'}
                    ]
                }
            },
            # {
            #     'name': 'Compliance Score',
            #     'type': 'summary',
            #     'options': {
            #         'value_options': {
            #             'key': 'value',
            #             'options': {
            #                 'default': 0
            #             }
            #         }
            #     },
            #     'query': {
            #         'aggregate': [
            #             {
            #                 'group': {
            #                     'fields': [
            #                         {
            #                             'key': 'data.stats.score.percent',
            #                             'name': 'value',
            #                             'operator': 'average'
            #                         }
            #                     ]
            #                 }
            #             }
            #         ],
            #         'filter': []
            #     }
            # },
        ],
        'sub_data': {
            'layouts': [
                {
                    'type': 'query-search-table',
                    'name': 'Checks',
                    'options': {
                        'unwind': {
                            'path': 'data.checks'
                        },
                        'default_sort': {
                            'key': 'data.checks.status',
                            'desc': False
                        },
                        'search': [
                            {
                                'key': 'data.requirement_id',
                                'name': 'Requirement ID'
                            },
                            {
                                'key': 'data.checks.check_title',
                                'name': 'Check Title'
                            },
                            {
                                'key': 'data.checks.status',
                                'name': 'Status',
                                'enums': [
                                    'FAIL',
                                    'PASS',
                                    'INFO'
                                ]
                            },
                            {
                                'key': 'data.checks.severity',
                                'name': 'Severity',
                                'enums': [
                                    'CRITICAL',
                                    'HIGH',
                                    'MEDIUM',
                                    'LOW',
                                    'INFORMATIONAL'
                                ]
                            },
                            {
                                'key': 'data.checks.service',
                                'name': 'Service'
                            }
                        ],
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'data.requirement_id',
                                'name': 'Requirement ID'
                            },
                            {
                                'type': 'text',
                                'key': 'data.checks.check_title',
                                'name': 'Check Title'
                            },
                            {
                                'type': 'enum',
                                'name': 'Status',
                                'key': 'data.checks.status',
                                'options': {
                                    'FAIL': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'coral.500'
                                        }
                                    },
                                    'PASS': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'indigo.500'
                                        }
                                    },
                                    'INFO': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'peacock.500'
                                        }
                                    }
                                }
                            },
                            {
                                'type': 'text',
                                'key': 'data.checks.display.findings',
                                'name': 'Findings',
                                'options': {
                                    'sortable': False
                                }
                            },
                            {
                                'type': 'text',
                                'key': 'data.checks.severity',
                                'name': 'Severity'
                            },
                            {
                                'type': 'text',
                                'key': 'data.checks.service',
                                'name': 'Service'
                            },
                            {
                                'type': 'text',
                                'key': 'data.checks.risk',
                                'name': 'Risk'
                            },
                            {
                                'type': 'text',
                                'key': 'data.checks.remediation.description',
                                'name': 'Remediation'
                            }
                        ]
                    }
                },
                {
                    'type': 'query-search-table',
                    'name': 'Findings',
                    'options': {
                        'unwind': {
                            'path': 'data.findings'
                        },
                        'default_sort': {
                            'key': 'data.findings.status',
                            'desc': False
                        },
                        'search': [
                            {
                                'key': 'data.requirement_id',
                                'name': 'Requirement ID'
                            },
                            {
                                'key': 'data.findings.check_title',
                                'name': 'Check Title'
                            },
                            {
                                'key': 'data.findings.status',
                                'name': 'Status',
                                'enums': [
                                    'FAIL',
                                    'PASS',
                                    'INFO'
                                ]
                            },
                            {
                                'key': 'data.findings.resource_type',
                                'name': 'Resource Type'
                            },
                            {
                                'key': 'data.findings.resource',
                                'name': 'Resource'
                            },
                            {
                                'key': 'data.findings.region_code',
                                'name': 'Region'
                            }
                        ],
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'data.requirement_id',
                                'name': 'Requirement ID'
                            },
                            {
                                'type': 'text',
                                'key': 'data.findings.check_title',
                                'name': 'Check Title'
                            },
                            {
                                'type': 'enum',
                                'name': 'Status',
                                'key': 'data.findings.status',
                                'options': {
                                    'FAIL': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'coral.500'
                                        }
                                    },
                                    'PASS': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'indigo.500'
                                        }
                                    },
                                    'INFO': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'peacock.500'
                                        }
                                    }
                                }
                            },
                            {
                                'type': 'text',
                                'key': 'data.findings.resource_type',
                                'name': 'Resource Type'
                            },
                            {
                                'type': 'text',
                                'key': 'data.findings.resource',
                                'name': 'Resource',
                                'reference': {
                                    'resource_type': 'inventory.CloudService',
                                    'reference_key': 'reference.resource_id'
                                }
                            },
                            {
                                'type': 'text',
                                'key': 'data.findings.region_code',
                                'name': 'Region',
                                'reference': {
                                    'resource_type': 'inventory.Region',
                                    'reference_key': 'region_code'
                                }
                            },
                            {
                                'type': 'text',
                                'key': 'data.findings.status_extended',
                                'name': 'Status Extended'
                            },
                        ]
                    }
                }
            ]
        }
    }
}


class CloudServiceType(BaseCloudServiceType):
    group: str = 'Prowler'
    is_primary: bool = True
    is_major: bool = True
    metadata: dict = _METADATA
    labels: List[str] = ['Security', 'Compliance']
    tags: dict = {
        'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/prowler.svg'
    }
