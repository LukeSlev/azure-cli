# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.testsdk import ScenarioTest


# Test class for Scenario
class PositiveTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(PositiveTest, self).__init__(*args, **kwargs)

    # EXAMPLE: /ApplicationGateways/post/Test Backend Health
    def test_application_gateway_backend_health_on_demand(self):
        self.cmd('az network application-gateway backend-health-on-demand '
                 '--name "appgw" '
                 '--path "/" '
                 '--sub-resource-id "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/applicationGateways/appgw/backendaddressPools/MFAnalyticsPool" '
                 '--id "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/applicationGateways/appgw/backendHttpSettingsCollection/MFPoolSettings" '
                 '--pick-host-name-from-backend-http-settings true '
                 '--timeout 30 '
                 '--protocol "Http" '
                 '--resource-group "rg1"')

    # EXAMPLE: /ApplicationGatewayPrivateEndpointConnections/get/Get Application Gateway Private Endpoint Connection
    def test_application_gateway_private(self):
        self.cmd('az network application-gateway-private-endpoint-connection show '
                 '--application-gateway-name "appgw" '
                 '--connection-name "connection1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /ApplicationSecurityGroups/get/List load balancers in resource group
    def test_application_security_group_list(self):
        self.cmd('az network application-security-group list '
                 '--resource-group "rg1"')

    # EXAMPLE: /WebCategories/get/List all Azure Web Categories for a given subscription
    def test_web_category_list(self):
        self.cmd('az network web-category list')

    # EXAMPLE: /network/post/GenerateVirtualWanVpnServerConfigurationVpnProfile
    def test_generatevirtualwanvpnserverconfigurationvpnpr(self):
        self.cmd('az network generatevirtualwanvpnserverconfigurationvpnprofile '
                 '--resource-group "rg1" '
                 '--virtual-wan-name "wan1" '
                 '--authentication-method "EAPTLS" '
                 '--vpn-server-configuration-resource-id "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/vpnServerConfigurations/vpnconfig1"')

    # EXAMPLE: /network/post/Returns a list of currently active sessions on the Bastion
    def test_get_active_session(self):
        self.cmd('az network get-active-session '
                 '--bastion-host-name "bastionhosttenant" '
                 '--resource-group "rg1"')

    # EXAMPLE: /network/get/supportedSecurityProviders
    def test_supported_security_provider(self):
        self.cmd('az network supported-security-provider '
                 '--resource-group "rg1" '
                 '--virtual-wan-name "wan1"')

    # EXAMPLE: /NetworkInterfaces/get/Get virtual machine scale set network interface
    def test_network_interface_show(self):
        self.cmd('az network network-interface show-virtual-machine-scale-set-ip-configuration '
                 '--ip-configuration-name "ip1" '
                 '--name "nic1" '
                 '--resource-group "rg1" '
                 '--virtual-machine-scale-set-name "vmss1" '
                 '--virtualmachine-index "2"')

    # EXAMPLE: /PublicIPAddresses/get/ListVMSSVMPublicIP
    def test_public_ip_address2(self):
        self.cmd('az network public-ip-address list-virtual-machine-scale-set-vm-public-ip-address '
                 '--ip-configuration-name "ip1" '
                 '--network-interface-name "nic1" '
                 '--resource-group "vmss-tester" '
                 '--virtual-machine-scale-set-name "vmss1" '
                 '--virtualmachine-index 1')

    # EXAMPLE: /PublicIPAddresses/get/GetVMSSPublicIP
    def test_public_ip_address(self):
        self.cmd('az network public-ip-address show-virtual-machine-scale-set-public-ip-address '
                 '--ip-configuration-name "ip1" '
                 '--network-interface-name "nic1" '
                 '--name "pub1" '
                 '--resource-group "vmss-tester" '
                 '--virtual-machine-scale-set-name "vmss1" '
                 '--virtualmachine-index 1')

    # EXAMPLE: /CustomIPPrefixes/get/List resource group Custom IP prefixes
    def test_custom_ip_prefix_list(self):
        self.cmd('az network custom-ip-prefix list '
                 '--resource-group "rg1"')

    # EXAMPLE: /CustomIPPrefixes/get/Get custom IP prefix
    def test_custom_ip_prefix_show(self):
        self.cmd('az network custom-ip-prefix show '
                 '--name "test-customipprefix" '
                 '--resource-group "rg1"')

    # EXAMPLE: /CustomIPPrefixes/get/List all custom IP prefixes
    def test_custom_ip_prefix_list_all(self):
        self.cmd('az network custom-ip-prefix list-all')

    # EXAMPLE: /ExpressRouteCircuitConnections/get/List ExpressRouteCircuit Connection
    def test_express_route_circuit_connection_list(self):
        self.cmd('az network express-route-circuit-connection list '
                 '--circuit-name "ExpressRouteARMCircuitA" '
                 '--peering-name "AzurePrivatePeering" '
                 '--resource-group "rg1"')

    # EXAMPLE: /ExpressRouteCircuits/post/List Route Table Summary
    def test_express_route_circuit(self):
        self.cmd('az network express-route-circuit list-route-table-summary '
                 '--circuit-name "circuitName" '
                 '--device-path "devicePath" '
                 '--peering-name "peeringName" '
                 '--resource-group "rg1"')

    # EXAMPLE: /ExpressRouteCircuits/get/Get ExpressRoute Circuit Peering Traffic Stats
    def test_express_route_circuit_show_peering_stat(self):
        self.cmd('az network express-route-circuit show-peering-stat '
                 '--circuit-name "circuitName" '
                 '--peering-name "peeringName" '
                 '--resource-group "rg1"')

    # EXAMPLE: /ExpressRouteCrossConnectionPeerings/get/GetExpressRouteCrossConnectionBgpPeering
    def test_express_route_cross_connection_peering_show(self):
        self.cmd('az network express-route-cross-connection-peering show '
                 '--cross-connection-name "<circuitServiceKey>" '
                 '--peering-name "AzurePrivatePeering" '
                 '--resource-group "CrossConnection-SiliconValley"')

    # EXAMPLE: /ExpressRouteCrossConnectionPeerings/put/ExpressRouteCrossConnectionBgpPeeringCreate
    def test_express_route_cross_connection_peering_create(self):
        self.cmd('az network express-route-cross-connection-peering create '
                 '--cross-connection-name "<circuitServiceKey>" '
                 '--peering-name "AzurePrivatePeering" '
                 '--ipv6-express-route-circuit-peering-config-primary-peer-address-prefix-primary-peer-address-prefix "3FFE:FFFF:0:CD30::/126" '
                 '--ipv6-express-route-circuit-peering-config-secondary-peer-address-prefix-secondary-peer-address-prefix "3FFE:FFFF:0:CD30::4/126" '
                 '--peer-asn 200 '
                 '--primary-peer-address-prefix "192.168.16.252/30" '
                 '--secondary-peer-address-prefix "192.168.18.252/30" '
                 '--vlan-id 200 '
                 '--resource-group "CrossConnection-SiliconValley"')

    # EXAMPLE: /ExpressRouteCrossConnectionPeerings/delete/DeleteExpressRouteCrossConnectionBgpPeering
    def test_express_route_cross_connection_peering_delete(self):
        self.cmd('az network express-route-cross-connection-peering delete -y '
                 '--cross-connection-name "<circuitServiceKey>" '
                 '--peering-name "AzurePrivatePeering" '
                 '--resource-group "CrossConnection-SiliconValley"')

    # EXAMPLE: /LoadBalancerFrontendIPConfigurations/get/LoadBalancerFrontendIPConfigurationList
    def test_load_balancer_frontend_ip_configuration_list(self):
        self.cmd('az network load-balancer-frontend-ip-configuration list '
                 '--load-balancer-name "lb" '
                 '--resource-group "testrg"')

    # EXAMPLE: /InboundNatRules/get/InboundNatRuleGet
    def test_inbound_nat_rule_show(self):
        self.cmd('az network inbound-nat-rule show '
                 '--name "natRule1.1" '
                 '--load-balancer-name "lb1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /InboundNatRules/put/InboundNatRuleCreate
    def test_inbound_nat_rule_create(self):
        self.cmd('az network inbound-nat-rule create '
                 '--inbound-nat-rule-name "natRule1.1" '
                 '--backend-port 3389 '
                 '--enable-floating-ip false '
                 '--enable-tcp-reset false '
                 '--sub-resource-id "/subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb1/frontendIPConfigurations/ip1" '
                 '--frontend-port 3390 '
                 '--idle-timeout-in-minutes 4 '
                 '--protocol "Tcp" '
                 '--load-balancer-name "lb1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /InboundNatRules/delete/InboundNatRuleDelete
    def test_inbound_nat_rule_delete(self):
        self.cmd('az network inbound-nat-rule delete -y '
                 '--name "natRule1.1" '
                 '--load-balancer-name "lb1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /LoadBalancerNetworkInterfaces/get/LoadBalancerNetworkInterfaceListSimple
    def test_load_balancer_network_interface_list(self):
        self.cmd('az network load-balancer-network-interface list '
                 '--load-balancer-name "lb" '
                 '--resource-group "testrg"')

    # EXAMPLE: /LoadBalancerNetworkInterfaces/get/LoadBalancerNetworkInterfaceListVmss
    def test_load_balancer_network_interface_list2(self):
        self.cmd('az network load-balancer-network-interface list '
                 '--load-balancer-name "lb" '
                 '--resource-group "testrg"')

    # EXAMPLE: /NetworkInterfaceIPConfigurations/get/NetworkInterfaceIPConfigurationList
    def test_network_interface_ip_configuration_list(self):
        self.cmd('az network network-interface-ip-configuration list '
                 '--network-interface-name "nic1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /NetworkInterfaceIPConfigurations/get/NetworkInterfaceIPConfigurationGet
    def test_network_interface_ip_configuration_show(self):
        self.cmd('az network network-interface-ip-configuration show '
                 '--ip-configuration-name "ipconfig1" '
                 '--network-interface-name "mynic" '
                 '--resource-group "testrg"')

    # EXAMPLE: /NetworkInterfaceLoadBalancers/get/NetworkInterfaceLoadBalancerList
    def test_network_interface_load_balancer_list(self):
        self.cmd('az network network-interface-load-balancer list '
                 '--network-interface-name "nic1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /NetworkInterfaceTapConfigurations/get/List virtual network tap configurations
    def test_network_interface_tap_configuration_list(self):
        self.cmd('az network network-interface-tap-configuration list '
                 '--network-interface-name "mynic" '
                 '--resource-group "rg1"')

    # EXAMPLE: /NetworkInterfaceTapConfigurations/delete/Delete tap configuration
    def test_network_interface_tap_configuration_delete(self):
        self.cmd('az network network-interface-tap-configuration delete -y '
                 '--network-interface-name "test-networkinterface" '
                 '--resource-group "rg1" '
                 '--tap-configuration-name "test-tapconfiguration"')

    # EXAMPLE: /DefaultSecurityRules/get/DefaultSecurityRuleList
    def test_default_security_rule_list(self):
        self.cmd('az network default-security-rule list '
                 '--nsg-name "nsg1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /DefaultSecurityRules/get/DefaultSecurityRuleGet
    def test_default_security_rule_show(self):
        self.cmd('az network default-security-rule show '
                 '--name "AllowVnetInBound" '
                 '--nsg-name "nsg1" '
                 '--resource-group "testrg"')

    # EXAMPLE: /NetworkWatchers/post/Get Azure Reachability Report
    def test_network_watcher_get_azure_reachability_report(self):
        self.cmd('az network network-watcher get-azure-reachability-report '
                 '--name "nw1" '
                 '--azure-locations "West US" '
                 '--end-time "2017-09-10T00:00:00Z" '
                 '--provider-location country="United States" state="washington" '
                 '--providers "Frontier Communications of America, Inc. - ASN 5650" '
                 '--start-time "2017-09-07T00:00:00Z" '
                 '--resource-group "rg1"')

    # EXAMPLE: /NetworkWatchers/post/Get Available Providers List
    def test_network_watcher_list_available_provider(self):
        self.cmd('az network network-watcher list-available-provider '
                 '--name "nw1" '
                 '--azure-locations "West US" '
                 '--city "seattle" '
                 '--country "United States" '
                 '--state "washington" '
                 '--resource-group "rg1"')

    # EXAMPLE: /PrivateLinkServices/get/List private link service in resource group
    def test_private_link_service2(self):
        self.cmd('az network private-link-service list-private-endpoint-connection '
                 '--resource-group "rg1" '
                 '--name "testPls"')

    # EXAMPLE: /PrivateLinkServices/get/Get private end point connection
    def test_private_link_service(self):
        self.cmd('az network private-link-service show-private-endpoint-connection '
                 '--pe-connection-name "testPlePeConnection" '
                 '--resource-group "rg1" '
                 '--name "testPls"')

    # EXAMPLE: /VirtualNetworks/get/VnetGetUsage
    def test_virtual_network_list_usage(self):
        self.cmd('az network virtual-network list-usage '
                 '--resource-group "rg1" '
                 '--name "vnetName"')

    # EXAMPLE: /Subnets/post/Prepare Network Policies
    def test_subnet_prepare_network_policy(self):
        self.cmd('az network subnet prepare-network-policy '
                 '--service-name "Microsoft.Sql/managedInstances" '
                 '--resource-group "rg1" '
                 '--name "subnet1" '
                 '--vnet-name "test-vnet"')

    # EXAMPLE: /Subnets/post/Unprepare Network Policies
    def test_subnet_unprepare_network_policy(self):
        self.cmd('az network subnet unprepare-network-policy '
                 '--resource-group "rg1" '
                 '--name "subnet1" '
                 '--service-name "Microsoft.Sql/managedInstances" '
                 '--vnet-name "test-vnet"')

    # EXAMPLE: /ResourceNavigationLinks/get/Get Resource Navigation Links
    def test_resource_navigation_link_list(self):
        self.cmd('az network resource-navigation-link list '
                 '--resource-group "rg1" '
                 '--subnet-name "subnet" '
                 '--vnet-name "vnet"')

    # EXAMPLE: /ServiceAssociationLinks/get/Get Service Association Links
    def test_service_association_link_list(self):
        self.cmd('az network service-association-link list '
                 '--resource-group "rg1" '
                 '--subnet-name "subnet" '
                 '--vnet-name "vnet"')

    # EXAMPLE: /VirtualNetworkGateways/post/Disconnect VpnConnections from Virtual Network Gateway
    def test_virtual_network_gateway5(self):
        self.cmd('az network virtual-network-gateway disconnect-virtual-network-gateway-vpn-connection '
                 '--resource-group "vpn-gateway-test" '
                 '--name "vpngateway" '
                 '--vpn-connection-ids "vpnconnId1" "vpnconnId2"')

    # EXAMPLE: /VirtualNetworkGateways/post/GetVirtualNetworkGatewayVpnclientConnectionHealth
    def test_virtual_network_gateway7(self):
        self.cmd('az network virtual-network-gateway get-vpnclient-connection-health '
                 '--resource-group "p2s-vnet-test" '
                 '--name "vpnp2sgw"')

    # EXAMPLE: /VirtualNetworkGateways/post/Get VirtualNetworkGateway VpnClientIpsecParameters
    def test_virtual_network_gateway6(self):
        self.cmd('az network virtual-network-gateway get-vpnclient-ipsec-parameter '
                 '--resource-group "rg1" '
                 '--name "vpngw"')

    # EXAMPLE: /VirtualNetworkGateways/get/VirtualNetworkGatewaysListConnections
    def test_virtual_network_gateway_list_connection(self):
        self.cmd('az network virtual-network-gateway list-connection '
                 '--resource-group "testrg" '
                 '--name "test-vpn-gateway-1"')

    # EXAMPLE: /VirtualNetworkGateways/post/Set VirtualNetworkGateway VpnClientIpsecParameters
    def test_virtual_network_gateway9(self):
        self.cmd('az network virtual-network-gateway set-vpnclient-ipsec-parameter '
                 '--resource-group "rg1" '
                 '--name "vpngw" '
                 '--dh-group "DHGroup2" '
                 '--ike-encryption "AES256" '
                 '--ike-integrity "SHA384" '
                 '--ipsec-encryption "AES256" '
                 '--ipsec-integrity "SHA256" '
                 '--pfs-group "PFS2" '
                 '--sa-data-size-kilobytes 429497 '
                 '--sa-life-time-seconds 86473')

    # EXAMPLE: /VirtualNetworkGateways/post/Start packet capture on virtual network gateway with filter
    def test_virtual_network_gateway_start_packet_capture(self):
        self.cmd('az network virtual-network-gateway start-packet-capture '
                 '--filter-data "{{\'TracingFlags\': 11,\'MaxPacketBufferSize\': 120,\'MaxFileSize\': 200,\'Filters\': [{{\'SourceSubnets\': [\'20.1.1.0/24\'],\'DestinationSubnets\': [\'10.1.1.0/24\'],\'SourcePort\': [500],\'DestinationPort\': [4500],\'Protocol\': 6,\'TcpFlags\': 16,\'CaptureSingleDirectionTrafficOnly\': true}}]}}" '
                 '--resource-group "rg1" '
                 '--name "vpngw"')

    # EXAMPLE: /VirtualNetworkGateways/post/Start packet capture on virtual network gateway without filter
    def test_virtual_network_gateway_start_packet_capture2(self):
        self.cmd('az network virtual-network-gateway start-packet-capture '
                 '--resource-group "rg1" '
                 '--name "vpngw"')

    # EXAMPLE: /VirtualNetworkGateways/post/Stop packet capture on virtual network gateway
    def test_virtual_network_gateway_stop_packet_capture(self):
        self.cmd('az network virtual-network-gateway stop-packet-capture '
                 '--sas-url "https://teststorage.blob.core.windows.net/?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-09-13T07:44:05Z&st=2019-09-06T23:44:05Z&spr=https&sig=V1h9D1riltvZMI69d6ihENnFo%2FrCvTqGgjO2lf%2FVBhE%3D" '
                 '--resource-group "rg1" '
                 '--name "vpngw"')

    # EXAMPLE: /VirtualNetworkGateways/post/ListVirtualNetworkGatewaySupportedVPNDevices
    def test_virtual_network_gateway_supported_vpn_device(self):
        self.cmd('az network virtual-network-gateway supported-vpn-device '
                 '--resource-group "rg1" '
                 '--name "vpngw"')

    # EXAMPLE: /VirtualNetworkGateways/post/GetVPNDeviceConfigurationScript
    def test_virtual_network_gateway8(self):
        self.cmd('az network virtual-network-gateway vpn-device-configuration-script '
                 '--device-family "ISR" '
                 '--firmware-version "IOS 15.1 (Preview)" '
                 '--vendor "Cisco" '
                 '--resource-group "rg1" '
                 '--virtual-network-gateway-connection-name "vpngw"')

    # EXAMPLE: /VirtualNetworkGatewayConnections/post/GetVirtualNetworkGatewayConnectionIkeSa
    def test_virtual_network_gateway(self):
        self.cmd('az network virtual-network-gateway-connection get-ike-sas '
                 '--resource-group "rg1" '
                 '--name "vpngwcn1"')

    # EXAMPLE: /VirtualNetworkGatewayConnections/post/Start packet capture on virtual network gateway connection with filter
    def test_virtual_network_gateway2(self):
        self.cmd('az network virtual-network-gateway-connection start-packet-capture '
                 '--filter-data "{{\'TracingFlags\': 11,\'MaxPacketBufferSize\': 120,\'MaxFileSize\': 200,\'Filters\': [{{\'SourceSubnets\': [\'20.1.1.0/24\'],\'DestinationSubnets\': [\'10.1.1.0/24\'],\'SourcePort\': [500],\'DestinationPort\': [4500],\'Protocol\': 6,\'TcpFlags\': 16,\'CaptureSingleDirectionTrafficOnly\': true}}]}}" '
                 '--resource-group "rg1" '
                 '--name "vpngwcn1"')

    # EXAMPLE: /VirtualNetworkGatewayConnections/post/Start packet capture on virtual network gateway connection without filter
    def test_virtual_network_gateway3(self):
        self.cmd('az network virtual-network-gateway-connection start-packet-capture '
                 '--resource-group "rg1" '
                 '--name "vpngwcn1"')

    # EXAMPLE: /VirtualNetworkGatewayConnections/post/Stop packet capture on virtual network gateway connection
    def test_virtual_network_gateway4(self):
        self.cmd('az network virtual-network-gateway-connection stop-packet-capture '
                 '--sas-url "https://teststorage.blob.core.windows.net/?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-09-13T07:44:05Z&st=2019-09-06T23:44:05Z&spr=https&sig=V1h9D1riltvZMI69d6ihENnFo%2FrCvTqGgjO2lf%2FVBhE%3D" '
                 '--resource-group "rg1" '
                 '--name "vpngwcn1"')

    # EXAMPLE: /VirtualNetworkTaps/get/List virtual network taps in resource group
    def test_virtual_network_tap_list(self):
        self.cmd('az network virtual-network-tap list '
                 '--resource-group "rg1"')

    # EXAMPLE: /VirtualNetworkTaps/get/Get Virtual Network Tap
    def test_virtual_network_tap_show(self):
        self.cmd('az network virtual-network-tap show '
                 '--resource-group "rg1" '
                 '--tap-name "testvtap"')

    # EXAMPLE: /VirtualNetworkTaps/delete/Delete Virtual Network Tap resource
    def test_virtual_network_tap_delete(self):
        self.cmd('az network virtual-network-tap delete -y '
                 '--resource-group "rg1" '
                 '--tap-name "test-vtap"')

    # EXAMPLE: /VpnSiteLinks/get/VpnSiteLinkListByVpnSite
    def test_vpn_site_link_list(self):
        self.cmd('az network vpn-site-link list '
                 '--resource-group "rg1" '
                 '--vpn-site-name "vpnSite1"')

    # EXAMPLE: /VpnSiteLinks/get/VpnSiteGet
    def test_vpn_site_link_show(self):
        self.cmd('az network vpn-site-link show '
                 '--resource-group "rg1" '
                 '--name "vpnSiteLink1" '
                 '--vpn-site-name "vpnSite1"')

    # EXAMPLE: /VpnGateways/post/ResetVpnGateway
    def test_vpn_gateway_reset(self):
        self.cmd('az network vpn-gateway reset '
                 '--gateway-name "vpngw" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VpnGateways/post/Start packet capture on vpn gateway with filter
    def test_vpn_gateway_start_packet_capture(self):
        self.cmd('az network vpn-gateway start-packet-capture '
                 '--gateway-name "vpngw" '
                 '--filter-data "{{\'TracingFlags\': 11,\'MaxPacketBufferSize\': 120,\'MaxFileSize\': 200,\'Filters\': [{{\'SourceSubnets\': [\'20.1.1.0/24\'],\'DestinationSubnets\': [\'10.1.1.0/24\'],\'SourcePort\': [500],\'DestinationPort\': [4500],\'Protocol\': 6,\'TcpFlags\': 16,\'CaptureSingleDirectionTrafficOnly\': true}}]}}" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VpnGateways/post/Start packet capture on vpn gateway without filter
    def test_vpn_gateway_start_packet_capture2(self):
        self.cmd('az network vpn-gateway start-packet-capture '
                 '--gateway-name "vpngw" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VpnGateways/post/Stop packet capture on vpn gateway
    def test_vpn_gateway_stop_packet_capture(self):
        self.cmd('az network vpn-gateway stop-packet-capture '
                 '--gateway-name "vpngw" '
                 '--sas-url "https://teststorage.blob.core.windows.net/?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-09-13T07:44:05Z&st=2019-09-06T23:44:05Z&spr=https&sig=V1h9D1riltvZMI69d6ihENnFo%2FrCvTqGgjO2lf%2FVBhE%3D" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VpnConnections/post/Start packet capture on vpn connection with filter
    def test_vpn_connection_start_packet_capture(self):
        self.cmd('az network vpn-connection start-packet-capture '
                 '--gateway-name "gateway1" '
                 '--filter-data "{{\'TracingFlags\': 11,\'MaxPacketBufferSize\': 120,\'MaxFileSize\': 200,\'Filters\': [{{\'SourceSubnets\': [\'20.1.1.0/24\'],\'DestinationSubnets\': [\'10.1.1.0/24\'],\'SourcePort\': [500],\'DestinationPort\': [4500],\'Protocol\': 6,\'TcpFlags\': 16,\'CaptureSingleDirectionTrafficOnly\': true}}]}}" '
                 '--link-connection-names "siteLink1" "siteLink2" '
                 '--resource-group "rg1" '
                 '--name "vpnConnection1"')

    # EXAMPLE: /VpnConnections/post/Start packet capture on vpn connection without filter
    def test_vpn_connection_start_packet_capture2(self):
        self.cmd('az network vpn-connection start-packet-capture '
                 '--gateway-name "gateway1" '
                 '--link-connection-names "siteLink1" "siteLink2" '
                 '--resource-group "rg1" '
                 '--name "vpnConnection1"')

    # EXAMPLE: /VpnConnections/post/Start packet capture on vpn connection without filter
    def test_vpn_connection_stop_packet_capture(self):
        self.cmd('az network vpn-connection stop-packet-capture '
                 '--gateway-name "gateway1" '
                 '--link-connection-names "vpnSiteLink1" "vpnSiteLink2" '
                 '--sas-url "https://teststorage.blob.core.windows.net/?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-09-13T07:44:05Z&st=2019-09-06T23:44:05Z&spr=https&sig=V1h9D1riltvZMI69d6ihENnFo%2FrCvTqGgjO2lf%2FVBhE%3D" '
                 '--resource-group "rg1" '
                 '--name "vpnConnection1"')

    # EXAMPLE: /VpnSiteLinkConnections/get/VpnSiteLinkConnectionGet
    def test_vpn_site_link_connection_show(self):
        self.cmd('az network vpn-site-link-connection show '
                 '--connection-name "vpnConnection1" '
                 '--gateway-name "gateway1" '
                 '--link-connection-name "Connection-Link1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /NatRules/get/NatRuleList
    def test_nat_rule_list(self):
        self.cmd('az network nat-rule list '
                 '--gateway-name "gateway1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /P2sVpnGateways/post/Disconnect VpnConnections from P2sVpn Gateway
    def test_p2_s_vpn(self):
        self.cmd('az network p2-s-vpn-gateway disconnect-p2-s-vpn-connection '
                 '--name "p2svpngateway" '
                 '--resource-group "p2s-vpn-gateway-test" '
                 '--vpn-connection-ids "vpnconnId1" "vpnconnId2"')

    # EXAMPLE: /P2sVpnGateways/post/P2SVpnGatewayGetConnectionHealth
    def test_p2_s_vpn2(self):
        self.cmd('az network p2-s-vpn-gateway get-p2-s-vpn-connection-health '
                 '--gateway-name "p2sVpnGateway1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /P2sVpnGateways/post/P2SVpnGatewayGetConnectionHealthDetailed
    def test_p2_s_vpn3(self):
        self.cmd('az network p2-s-vpn-gateway get-p2-s-vpn-connection-health-detailed '
                 '--gateway-name "p2svpngateway" '
                 '--resource-group "p2s-vpn-gateway-test" '
                 '--output-blob-sas-url "https://blobcortextesturl.blob.core.windows.net/folderforconfig/p2sconnectionhealths?sp=rw&se=2018-01-10T03%3A42%3A04Z&sv=2017-04-17&sig=WvXrT5bDmDFfgHs%2Brz%2BjAu123eRCNE9BO0eQYcPDT7pY%3D&sr=b" '
                 '--vpn-user-names-filter "vpnUser1" "vpnUser2"')

    # EXAMPLE: /P2sVpnGateways/post/ResetP2SVpnGateway
    def test_p2_s_vpn_gateway_reset(self):
        self.cmd('az network p2-s-vpn-gateway reset '
                 '--gateway-name "p2sVpnGateway1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VpnServerConfigurationsAssociatedWithVirtualWan/post/GetVirtualWanVpnServerConfigurations
    def test_vpn_server_configuration(self):
        self.cmd('az network vpn-server-configuration-associated-with-virtual-wan list '
                 '--resource-group "rg1" '
                 '--virtual-wan-name "wan1"')

    # EXAMPLE: /VirtualHubBgpConnection/delete/VirtualHubRouteTableV2Delete
    def test_virtual_hub_bgp_connection_delete(self):
        self.cmd('az network virtual-hub-bgp-connection delete -y '
                 '--connection-name "conn1" '
                 '--resource-group "rg1" '
                 '--virtual-hub-name "hub1"')

    # EXAMPLE: /VirtualHubBgpConnections/post/VirtualRouterPeerListAdvertisedRoutes
    def test_virtual_hub_bgp(self):
        self.cmd('az network virtual-hub-bgp-connection list-advertised-route '
                 '--connection-name "peer1" '
                 '--hub-name "virtualRouter1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VirtualHubBgpConnections/post/VirtualRouterPeerListLearnedRoutes
    def test_virtual_hub_bgp_connection_list_learned_route(self):
        self.cmd('az network virtual-hub-bgp-connection list-learned-route '
                 '--connection-name "peer1" '
                 '--hub-name "virtualRouter1" '
                 '--resource-group "rg1"')

    # EXAMPLE: /VirtualHubIpConfiguration/get/VirtualHubRouteTableV2List
    def test_virtual_hub_ip_configuration_list(self):
        self.cmd('az network virtual-hub-ip-configuration list '
                 '--resource-group "rg1" '
                 '--virtual-hub-name "hub1"')
