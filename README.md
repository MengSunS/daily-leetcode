# Elasticsearch Helm Chart

This Helm chart is a lightweight way to configure and run our official
[Elasticsearch Docker image][].



<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Requirements](#requirements)
- [Installing](#installing)
  - [Download helm charts](#download-helm-charts)
  - [Install elasticsearch helm charts](#install-elasticsearch-helm-charts)
  - [Installed components](#installed-components)
  - [Uninstalling the chart](#uninstalling-the-chart)
- [Upgrading](#upgrading)
- [Usage notes](#usage-notes)
- [Configuration](#configuration)
  - [Deprecated](#deprecated)
- [FAQ](#faq)
  - [How to deploy this chart on a specific K8S distribution?](#how-to-deploy-this-chart-on-a-specific-k8s-distribution)
  - [How to deploy dedicated nodes types?](#how-to-deploy-dedicated-nodes-types)
    - [Clustering and Node Discovery](#clustering-and-node-discovery)
  - [How to deploy clusters with security (authentication and TLS) enabled?](#how-to-deploy-clusters-with-security-authentication-and-tls-enabled)
  - [How to migrate from helm/charts stable chart?](#how-to-migrate-from-helmcharts-stable-chart)
  - [How to install OSS version of Elasticsearch?](#how-to-install-oss-version-of-elasticsearch)
  - [How to install plugins?](#how-to-install-plugins)
  - [How to use the keystore?](#how-to-use-the-keystore)
    - [Basic example](#basic-example)
    - [Multiple keys](#multiple-keys)
    - [Custom paths and keys](#custom-paths-and-keys)
  - [How to enable snapshotting?](#how-to-enable-snapshotting)
  - [How to configure templates post-deployment?](#how-to-configure-templates-post-deployment)
- [Notes](#notes)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


## Requirements

* [Helm][] >=2.8.0 and <3.0.0
* Kubernetes >=1.8
* Minimum cluster requirements include the following to run this chart with
default settings. All of these settings are configurable.
  * Three Kubernetes nodes to respect the default "hard" affinity settings
  * 1GB of RAM for the JVM heap

See [supported configurations][] for more details.

## Installing

This chart is tested with the latest 7.9.2 version.

### Download helm charts

```console
$ helm repo add atom-helm https://svl-artifactory.juniper.net/atom-helm
$ helm repo update
$ helm fetch atom-helm/elasticsearch --version=1.0.1-g34a44d5557
```
### Install elasticsearch helm charts

```console
helm install atom-helm/elasticsearch --version=1.0.1-g34a44d5557 --namespace logging -n elasticsearch
```

You can specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

Alternatively, a YAML file that specifies the values for the parameters can be provided while installing the chart. For example,

```console
helm install --name elasticsearch -f my-values.yaml atom-helm/elasticsearch
```

> **Tip**: A default [values.yaml](values.yaml) is provided

### Installed components

You can use `kubectl get all -n logging` to view all of the installed components.

For example:

```console

helm install atom-helm/elasticsearch --version=1.0.1-g34a44d5557 --namespace logging -n elasticsearch --set replicas=1

NAME:   elasticsearch
LAST DEPLOYED: Tue Nov 10 14:24:19 2020
NAMESPACE: logging
STATUS: DEPLOYED

RESOURCES:
==> v1/Pod(related)
NAME                    READY  STATUS   RESTARTS  AGE
elasticsearch-master-0  1/1    Running  0         0s

==> v1/Service
NAME                           TYPE       CLUSTER-IP     EXTERNAL-IP  PORT(S)            AGE
elasticsearch-master           ClusterIP  10.109.237.15  <none>       9200/TCP,9300/TCP  0s
elasticsearch-master-headless  ClusterIP  None           <none>       9200/TCP,9300/TCP  0s

==> v1/StatefulSet
NAME                  READY  AGE
elasticsearch-master  1/1    0s

==> v1beta1/PodDisruptionBudget
NAME                      MIN AVAILABLE  MAX UNAVAILABLE  ALLOWED DISRUPTIONS  AGE
elasticsearch-master-pdb  N/A            1                0                    1s

```
### Uninstalling the chart

```console
$ helm delete elasticsearch --purge
```
## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Usage notes

* This repo includes a number of [examples][] configurations which can be used
as a reference. They are also used in the automated testing of this chart.
* Automated testing of this chart is currently only run against GKE (Google
Kubernetes Engine).
* The chart deploys a StatefulSet and by default will do an automated rolling
update of your cluster. It does this by waiting for the cluster health to become
green after each instance is updated. If you prefer to update manually you can
set `OnDelete` [updateStrategy][].
* It is important to verify that the JVM heap size in `esJavaOpts` and to set
the CPU/Memory `resources` to something suitable for your cluster.
* To simplify chart and maintenance each set of node groups is deployed as a
separate Helm release. Take a look at the [multi][] example to get an idea for
how this works. Without doing this it isn't possible to resize persistent
volumes in a StatefulSet. By setting it up this way it makes it possible to add
more nodes with a new storage size then drain the old ones. It also solves the
problem of allowing the user to determine which node groups to update first when
doing upgrades or changes.
* We have designed this chart to be very un-opinionated about how to configure
Elasticsearch. It exposes ways to set environment variables and mount secrets
inside of the container. Doing this makes it much easier for this chart to
support multiple versions with minimal changes.


## Configuration

| Parameter                          | Description                                                                                                                                                                                                                                               | Default                                         |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `antiAffinityTopologyKey`          | The [anti-affinity][] topology key. By default this will prevent multiple Elasticsearch nodes from running on the same Kubernetes node                                                                                                                    | `kubernetes.io/hostname`                        |
| `antiAffinity`                     | Setting this to hard enforces the [anti-affinity][] rules. If it is set to soft it will be done "best effort". Other values will be ignored                                                                                                               | `hard`                                          |
| `clusterHealthCheckParams`         | The [Elasticsearch cluster health status params][] that will be used by readiness [probe][] command                                                                                                                                                       | `wait_for_status=green&timeout=1s`              |
| `clusterName`                      | This will be used as the Elasticsearch [cluster.name][] and should be unique per cluster in the namespace                                                                                                                                                 | `elasticsearch`                                 |
| `enableServiceLinks`               | Set to false to disabling service links, which can cause slow pod startup times when there are many services in the current namespace.                                                                                                                    | `true`                                          |
| `envFrom`                          | Templatable string to be passed to the [environment from variables][] which will be appended to the `envFrom:` definition for the container                                                                                                               | `[]`                                            |
| `esConfig`                         | Allows you to add any config files in `/usr/share/elasticsearch/config/` such as `elasticsearch.yml` and `log4j2.properties`. See [values.yaml][] for an example of the formatting                                                                        | `{}`                                            |
| `esJavaOpts`                       | [Java options][] for Elasticsearch. This is where you should configure the [jvm heap size][]                                                                                                                                                              | `-Xmx1g -Xms1g`                                 |
| `esMajorVersion`                   | Used to set major version specific configuration. If you are using a custom image and not running the default Elasticsearch version you will need to set this to the version you are running (e.g. `esMajorVersion: 6`)                                   | `""`                                            |
| `extraContainers`                  | Templatable string of additional `containers` to be passed to the `tpl` function                                                                                                                                                                          | `""`                                            |
| `extraEnvs`                        | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                                                                                                                         | `[]`                                            |
| `extraInitContainers`              | Templatable string of additional `initContainers` to be passed to the `tpl` function                                                                                                                                                                      | `""`                                            |
| `extraVolumeMounts`                | Templatable string of additional `volumeMounts` to be passed to the `tpl` function                                                                                                                                                                        | `""`                                            |
| `extraVolumes`                     | Templatable string of additional `volumes` to be passed to the `tpl` function                                                                                                                                                                             | `""`                                            |
| `fullnameOverride`                 | Overrides the `clusterName` and `nodeGroup` when used in the naming of resources. This should only be used when using a single `nodeGroup`, otherwise you will have name conflicts                                                                        | `""`                                            |
| `httpPort`                         | The http port that Kubernetes will use for the healthchecks and the service. If you change this you will also need to set [http.port][] in `extraEnvs`                                                                                                    | `9200`                                          |
| `imagePullPolicy`                  | The Kubernetes [imagePullPolicy][] value                                                                                                                                                                                                                  | `IfNotPresent`                                  |
| `imagePullSecrets`                 | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                                                                                                                              | `[]`                                            |
| `imageTag`                         | The Elasticsearch Docker image tag                                                                                                                                                                                                                        | `7.9.2`                                |
| `image`                            | The Elasticsearch Docker image                                                                                                                                                                                                                            | `docker.elastic.co/elasticsearch/elasticsearch` |
| `ingress`                          | Configurable [ingress][] to expose the Elasticsearch service. See [values.yaml][] for an example                                                                                                                                                          | see [values.yaml][]                             |
| `initResources`                    | Allows you to set the [resources][] for the `initContainer` in the StatefulSet                                                                                                                                                                            | `{}`                                            |
| `keystore`                         | Allows you map Kubernetes secrets into the keystore. See the [config example][] and [how to use the keystore][]                                                                                                                                           | `[]`                                            |
| `labels`                           | Configurable [labels][] applied to all Elasticsearch pods                                                                                                                                                                                                 | `{}`                                            |
| `lifecycle`                        | Allows you to add [lifecycle hooks][]. See [values.yaml][] for an example of the formatting                                                                                                                                                               | `{}`                                            |
| `masterService`                    | The service name used to connect to the masters. You only need to set this if your master `nodeGroup` is set to something other than `master`. See [Clustering and Node Discovery][] for more information                                                 | `""`                                            |
| `masterTerminationFix`             | A workaround needed for Elasticsearch < 7.2 to prevent master status being lost during restarts [#63][]                                                                                                                                                   | `false`                                         |
| `maxUnavailable`                   | The [maxUnavailable][] value for the pod disruption budget. By default this will prevent Kubernetes from having more than 1 unhealthy pod in the node group                                                                                               | `1`                                             |
| `minimumMasterNodes`               | The value for [discovery.zen.minimum_master_nodes][]. Should be set to `(master_eligible_nodes / 2) + 1`. Ignored in Elasticsearch versions >= 7                                                                                                          | `2`                                             |
| `nameOverride`                     | Overrides the `clusterName` when used in the naming of resources                                                                                                                                                                                          | `""`                                            |
| `networkHost`                      | Value for the [network.host Elasticsearch setting][]                                                                                                                                                                                                      | `0.0.0.0`                                       |
| `nodeAffinity`                     | Value for the [node affinity settings][]                                                                                                                                                                                                                  | `{}`                                            |
| `nodeGroup`                        | This is the name that will be used for each group of nodes in the cluster. The name will be `clusterName-nodeGroup-X` , `nameOverride-nodeGroup-X` if a `nameOverride` is specified, and `fullnameOverride-X` if a `fullnameOverride` is specified        | `master`                                        |
| `nodeSelector`                     | Configurable [nodeSelector][] so that you can target specific nodes for your Elasticsearch cluster                                                                                                                                                        | `{}`                                            |
| `persistence`                      | Enables a persistent volume for Elasticsearch data. Can be disabled for nodes that only have [roles][] which don't require persistent data                                                                                                                | see [values.yaml][]                             |
| `podAnnotations`                   | Configurable [annotations][] applied to all Elasticsearch pods                                                                                                                                                                                            | `{}`                                            |
| `podManagementPolicy`              | By default Kubernetes [deploys StatefulSets serially][]. This deploys them in parallel so that they can discover each other                                                                                                                               | `Parallel`                                      |
| `podSecurityContext`               | Allows you to set the [securityContext][] for the pod                                                                                                                                                                                                     | see [values.yaml][]                             |
| `podSecurityPolicy`                | Configuration for create a pod security policy with minimal permissions to run this Helm chart with `create: true`. Also can be used to reference an external pod security policy with `name: "externalPodSecurityPolicy"`                                | see [values.yaml][]                             |
| `priorityClassName`                | The name of the [PriorityClass][]. No default is supplied as the PriorityClass must be created first                                                                                                                                                      | `""`                                            |
| `protocol`                         | The protocol that will be used for the readiness [probe][]. Change this to `https` if you have `xpack.security.http.ssl.enabled` set                                                                                                                      | `http`                                          |
| `rbac`                             | Configuration for creating a role, role binding and ServiceAccount as part of this Helm chart with `create: true`. Also can be used to reference an external ServiceAccount with `serviceAccountName: "externalServiceAccountName"`                       | see [values.yaml][]                             |
| `readinessProbe`                   | Configuration fields for the readiness [probe][]                                                                                                                                                                                                          | see [values.yaml][]                             |
| `replicas`                         | Kubernetes replica count for the StatefulSet (i.e. how many pods)                                                                                                                                                                                         | `3`                                             |
| `resources`                        | Allows you to set the [resources][] for the StatefulSet                                                                                                                                                                                                   | see [values.yaml][]                             |
| `roles`                            | A hash map with the specific [roles][] for the `nodeGroup`                                                                                                                                                                                                | see [values.yaml][]                             |
| `schedulerName`                    | Name of the [alternate scheduler][]                                                                                                                                                                                                                       | `""`                                            |
| `secretMounts`                     | Allows you easily mount a secret as a file inside the StatefulSet. Useful for mounting certificates and other secrets. See [values.yaml][] for an example                                                                                                 | `[]`                                            |
| `securityContext`                  | Allows you to set the [securityContext][] for the container                                                                                                                                                                                               | see [values.yaml][]                             |
| `service.annotations`              | [LoadBalancer annotations][] that Kubernetes will use for the service. This will configure load balancer if `service.type` is `LoadBalancer`                                                                                                              | `{}`                                            |
| `service.externalTrafficPolicy`              | Some cloud providers allow you to specify the [LoadBalancer externalTrafficPolicy][]. Kubernetes will use this to preserve the client source IP. This will configure load balancer if `service.type` is `LoadBalancer`                                                                                                              | `""`                                            |
| `service.httpPortName`             | The name of the http port within the service                                                                                                                                                                                                              | `http`                                          |
| `service.labelsHeadless`           | Labels to be added to headless service                                                                                                                                                                                                                    | `{}`                                            |
| `service.labels`                   | Labels to be added to non-headless service                                                                                                                                                                                                                | `{}`                                            |
| `service.loadBalancerIP`           | Some cloud providers allow you to specify the [loadBalancer][] IP. If the `loadBalancerIP` field is not specified, the IP is dynamically assigned. If you specify a `loadBalancerIP` but your cloud provider does not support the feature, it is ignored. | `""`                                            |
| `service.loadBalancerSourceRanges` | The IP ranges that are allowed to access                                                                                                                                                                                                                  | `[]`                                            |
| `service.nodePort`                 | Custom [nodePort][] port that can be set if you are using `service.type: nodePort`                                                                                                                                                                        | `""`                                            |
| `service.transportPortName`        | The name of the transport port within the service                                                                                                                                                                                                         | `transport`                                     |
| `service.type`                     | Elasticsearch [Service Types][]                                                                                                                                                                                                                           | `ClusterIP`                                     |
| `sidecarResources`                 | Allows you to set the [resources][] for the sidecar containers in the StatefulSet                                                                                                                                                                         | {}                                              |
| `sysctlInitContainer`              | Allows you to disable the `sysctlInitContainer` if you are setting [sysctl vm.max_map_count][] with another method                                                                                                                                        | `enabled: true`                                 |
| `sysctlVmMaxMapCount`              | Sets the [sysctl vm.max_map_count][] needed for Elasticsearch                                                                                                                                                                                             | `262144`                                        |
| `terminationGracePeriod`           | The [terminationGracePeriod][] in seconds used when trying to stop the pod                                                                                                                                                                                | `120`                                           |
| `tolerations`                      | Configurable [tolerations][]                                                                                                                                                                                                                              | `[]`                                            |
| `transportPort`                    | The transport port that Kubernetes will use for the service. If you change this you will also need to set [transport port configuration][] in `extraEnvs`                                                                                                 | `9300`                                          |
| `updateStrategy`                   | The [updateStrategy][] for the StatefulSet. By default Kubernetes will wait for the cluster to be green after upgrading each pod. Setting this to `OnDelete` will allow you to manually delete each pod during upgrades                                   | `RollingUpdate`                                 |
| `volumeClaimTemplate`              | Configuration for the [volumeClaimTemplate for StatefulSets][]. You will want to adjust the storage (default `30Gi` ) and the `storageClassName` if you are using a different storage class                                                               | see [values.yaml][]                             |
| `metrics.enabled`                  		| enable Prometheus                                                                                                                                                   										 | `false`					   |
| `metrics.name`                     		| exporter name 																												 | `exporter`    				   |
| `metrics.replicas` 		     		| Kubernetes replica count for the exporter deployments 																							 | `1`						   |
| `metrics.affinity` 		     		| Setting this to hard enforces the [affinity][] rules. If it is set to soft it will be done "best effort". Other values will be ignored    													 | `hard`					   |
| `metrics.restartPolicy` 	     		| restart policy 																												 | `Always`					   |
| `metrics.image.repository` 	     		| container image repository 																											 |  see [values.yaml][]				   |
| `metrics.image.tag` 	             		| container image tag 																												 | `1.1.0`					   |
| `metrics.image.pullPolicy` 	     		| container image pull policy 																											 | `IfNotPresent`				   |
| `metrics.image.pullSecret` 	     		| container image pull secret 																											 | `""`  					   |
| `metrics.log.format` 		     		| Format used for the logs. Valid formats are `json` and `logfmt` 																						 | `logfmt`					   |
| `metrics.log.level` 		     		| Logging level to be used. Valid levels are `debug`, `info`, `warn`, `error` 																					 | `info`					   |
| `metrics.resources` 		     		| resource requests & limits 																											 | see [values.yaml][]				   |
| `metrics.priorityClassName` 	     		| priorityClassName 																												 | `nil`					   |
| `metrics.nodeSelector` 	     		| Node labels for pod assignment 																										 | `{}`						   |
| `metrics.tolerations` 	     		| Node tolerations for pod assignment 																										 | `{}`						   |
| `metrics.podAnnotations` 	     		| Pod annotations 																												 | `{}` 					   |
| `metrics.service.type` 	     		| type of service to create 																											 | `ClusterIP`					   |
| `metrics.service.httpPort` 	     		| port for the http service 																											 | `9108`					   |
| `metrics.service.metricsPort.name` 		| name for the http service 																											 | `http`					   |
| `metrics.service.annotations`      		| Annotations on the http service 																										 | `{}`						   |
| `metrics.service.labels` 	     		| Additional labels for the service definition 																									 | `{}`						   |
| `metrics.env` 	             		| Extra environment variables passed to pod 																								         | `{}`						   |
| `metrics.envFromSecret` 	     		| The name of an existing secret in the same kubernetes namespace which contains values to be added to the environment 															         | `nil`					   |
| `metrics.extraEnvSecrets` 	     		| Extra environment variables passed to the pod from k8s secrets - see `values.yaml` for an example 																		 | `{}` 					   |
| `metrics.secretMounts` 	     		|  list of secrets and their paths to mount inside the pod 																						         | `[]`						   |
| `metrics.es.uri` 	             		| address of the Elasticsearch node to connect to 																								 | `http://elasticsearch-master.logging:9200`      |
| `metrics.es.all` 	             		| if `true`, query stats for all nodes in the cluster, rather than just the node we connect to 																			 | `true` 				           |
| `metrics.es.indices` 		     		| if true, query stats for all indices in the cluster 																								 | `true`					   |
| `metrics.es.indices_settings`      		| if true, query settings stats for all indices in the cluster 																							 | `true`					   |
| `metrics.es.shards` 		     		| if true, query stats for shards in the cluster 																								 | `true`					   |
| `metrics.es.cluster_settings`      		| if true, query stats for cluster settings 																									 | `false`					   |
| `metrics.es.snapshots` 	     		| if true, query stats for snapshots in the cluster 																								 | `true`					   |
| `metrics.es.timeout` 	  	     		| timeout for trying to get stats from Elasticsearch 																								 | `30s`					   |
| `metrics.es.ssl.enabled` 	     		| If true, a secure connection to Elasticsearch cluster is used 																						 | `false`					   |
| `metrics.es.ssl.useExistingSecrets`		| If true, certs from secretMounts will be used 																								 | `false`					   |
| `metrics.es.ssl.ca.pem` 	     		| PEM that contains trusted CAs used for setting up secure Elasticsearch connection 																				 |						   |
| `metrics.es.ssl.ca.path` 	     		| Path of ca pem file which should match a secretMount path 																							 |						   |
| `metrics.es.ssl.client.enabled`    		| If true, use SSL client certificates for authentication 																							 | `true`					   |
| `metrics.es.ssl.client.pem` 	     		| PEM that contains the client cert to connect to Elasticsearch 																						 |						   |
| `metrics.es.ssl.client.pemPath`    		| Path of client pem file which should match a secretMount path 																						 |						   |
| `metrics.es.ssl.client.key` 	     		| Private key for client auth when connecting to Elasticsearch 																							 |						   |
| `metrics.es.ssl.client.keyPath`   		| Path of client key file which should match a secretMount path 																						 |						   |
| `metrics.web.path` 		    		| path under which to expose metrics 																										 | `/metrics`					   |
| `metrics.serviceMonitor.enabled`  		| If true, a ServiceMonitor CRD is created for a prometheus operator 																						 | `false`					   |
| `metrics.serviceMonitor.namespace` 		| If set, the ServiceMonitor will be installed in a different namespace  																					 | `""`						   |
| `metrics.serviceMonitor.labels`    		| Labels for prometheus operator 																										 | `{}`						   |
| `metrics.serviceMonitor.interval`  		| Interval at which metrics should be scraped 																									 | `10s`					   |
| `metrics.serviceMonitor.scrapeTimeout`  	| Timeout after which the scrape is ended 																									 | `10s`					   |
| `metrics.serviceMonitor.scheme`    		| Scheme to use for scraping 																											 | `http`					   |
| `metrics.serviceMonitor.relabelings` 		| Relabel configuration for the metrics 																									 | `[]`						   |
| `metrics.serviceMonitor.targetLabels` 	| Set of labels to transfer on the Kubernetes Service onto the target. 																						 | `[]` 					   |
| `metrics.serviceMonitor.metricRelabelings`	| MetricRelabelConfigs to apply to samples before ingestion. 																							 | `[]`						   |
| `metrics.serviceMonitor.sampleLimit` 		| Number of samples that will fail the scrape if exceeded 																							 | `0`						   |
| `metrics.prometheusRule.enabled` 		| If true, a PrometheusRule CRD is created for a prometheus operator 																						 | `false`					   |
| `metrics.prometheusRule.namespace` 		| If set, the PrometheusRule will be installed in a different namespace  																					 | `""` 					   |
| `metrics.prometheusRule.labels` 		| Labels for prometheus operator 																										 | `{}`						   |
| `metrics.prometheusRule.rules` 		| List of [PrometheusRules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) to be created, check values for an example. 												 | `[]` 					   |
| `metrics.serviceAccount.create` 		| Create a ServiceAccount for the pod | `false`
| `metrics.serviceAccount.name` 		| Name of a ServiceAccount to use that is not handled by this chart | `default`
| `metrics.podSecurityPolicies.enabled` 	| Enable/disable PodSecurityPolicy and associated Role/Rolebinding creation | `false`


### Deprecated

| Parameter | Description                                                                                                   | Default |
|-----------|---------------------------------------------------------------------------------------------------------------|---------|
| `fsGroup` | The Group ID (GID) for [securityContext][] so that the Elasticsearch user can read from the persistent volume | `""`    |


## FAQ

### How to deploy this chart on a specific K8S distribution?

This chart is designed to run on production scale Kubernetes clusters with
multiple nodes, lots of memory and persistent storage. For that reason it can be
a bit tricky to run them against local Kubernetes environments such as
[Minikube][].

This chart is highly tested with [GKE][], but some K8S distribution also
requires specific configurations.

We provide examples of configuration for the following K8S providers:

- [Docker for Mac][]
- [KIND][]
- [Minikube][]
- [MicroK8S][]
- [OpenShift][]

### How to deploy dedicated nodes types?

All the Elasticsearch pods deployed share the same configuration. If you need to
deploy dedicated [nodes types][] (for example dedicated master and data nodes),
you can deploy multiple releases of this chart with different configurations
while they share the same `clusterName` value.

For each Helm release, the nodes types can then be defined using `roles` value.

An example of Elasticsearch cluster using 2 different Helm releases for master
and data nodes can be found in [examples/multi][].

#### Clustering and Node Discovery

This chart facilitates Elasticsearch node discovery and services by creating two
`Service` definitions in Kubernetes, one with the name `$clusterName-$nodeGroup`
and another named `$clusterName-$nodeGroup-headless`.
Only `Ready` pods are a part of the `$clusterName-$nodeGroup` service, while all
pods ( `Ready` or not) are a part of `$clusterName-$nodeGroup-headless`.

If your group of master nodes has the default `nodeGroup: master` then you can
just add new groups of nodes with a different `nodeGroup` and they will
automatically discover the correct master. If your master nodes have a different
`nodeGroup` name then you will need to set `masterService` to
`$clusterName-$masterNodeGroup`.

The chart value for `masterService` is used to populate
`discovery.zen.ping.unicast.hosts` , which Elasticsearch nodes will use to
contact master nodes and form a cluster.
Therefore, to add a group of nodes to an existing cluster, setting
`masterService` to the desired `Service` name of the related cluster is
sufficient.

### How to deploy clusters with security (authentication and TLS) enabled?

This Helm chart can use existing [Kubernetes secrets][] to setup
credentials or certificates for examples. These secrets should be created
outside of this chart and accessed using [environment variables][] and volumes.

An example of Elasticsearch cluster using security can be found in
[examples/security][].

### How to migrate from helm/charts stable chart?

If you currently have a cluster deployed with the [helm/charts stable][] chart
you can follow the [migration guide][].

### How to install OSS version of Elasticsearch?

Deploying OSS version of Elasticsearch can be done by setting `image` value to
[Elasticsearch OSS Docker image][]

An example of Elasticsearch cluster using OSS version can be found in
[examples/oss][].

### How to install plugins?

The recommended way to install plugins into our Docker images is to create a
[custom Docker image][].

The Dockerfile would look something like:

```
ARG elasticsearch_version
FROM docker.elastic.co/elasticsearch/elasticsearch:${elasticsearch_version}

RUN bin/elasticsearch-plugin install --batch repository-gcs
```

And then updating the `image` in values to point to your custom image.

There are a couple reasons we recommend this.

1. Tying the availability of Elasticsearch to the download service to install
plugins is not a great idea or something that we recommend. Especially in
Kubernetes where it is normal and expected for a container to be moved to
another host at random times.
2. Mutating the state of a running Docker image (by installing plugins) goes
against best practices of containers and immutable infrastructure.

### How to use the keystore?

#### Basic example

Create the secret, the key name needs to be the keystore key path. In this
example we will create a secret from a file and from a literal string.

```
kubectl create secret generic encryption-key --from-file=xpack.watcher.encryption_key=./watcher_encryption_key
kubectl create secret generic slack-hook --from-literal=xpack.notification.slack.account.monitoring.secure_url='https://hooks.slack.com/services/asdasdasd/asdasdas/asdasd'
```

To add these secrets to the keystore:

```
keystore:
  - secretName: encryption-key
  - secretName: slack-hook
```

#### Multiple keys

All keys in the secret will be added to the keystore. To create the previous
example in one secret you could also do:

```
kubectl create secret generic keystore-secrets --from-file=xpack.watcher.encryption_key=./watcher_encryption_key --from-literal=xpack.notification.slack.account.monitoring.secure_url='https://hooks.slack.com/services/asdasdasd/asdasdas/asdasd'
```

```
keystore:
  - secretName: keystore-secrets
```

#### Custom paths and keys

If you are using these secrets for other applications (besides the Elasticsearch
keystore) then it is also possible to specify the keystore path and which keys
you want to add. Everything specified under each `keystore` item will be passed
through to the `volumeMounts` section for mounting the [secret][]. In this
example we will only add the `slack_hook` key from a secret that also has other
keys. Our secret looks like this:

```
kubectl create secret generic slack-secrets --from-literal=slack_channel='#general' --from-literal=slack_hook='https://hooks.slack.com/services/asdasdasd/asdasdas/asdasd'
```

We only want to add the `slack_hook` key to the keystore at path
`xpack.notification.slack.account.monitoring.secure_url`:

```
keystore:
  - secretName: slack-secrets
    items:
    - key: slack_hook
      path: xpack.notification.slack.account.monitoring.secure_url
```

You can also take a look at the [config example][] which is used as part of the
automated testing pipeline.

### How to enable snapshotting?

1. Install your [snapshot plugin][] into a custom Docker image following the
[how to install plugins guide][].
2. Add any required secrets or credentials into an Elasticsearch keystore
following the [how to use the keystore][] guide.
3. Configure the [snapshot repository][] as you normally would.
4. To automate snapshots you can use [Snapshot Lifecycle Management][] or a tool
like [curator][].

### How to configure templates post-deployment?

You can use `postStart` [lifecycle hooks][] to run code triggered after a
container is created.

Here is an example of `postStart` hook to configure templates:

```yaml
lifecycle:
  postStart:
    exec:
      command:
        - bash
        - -c
        - |
          #!/bin/bash
          # Add a template to adjust number of shards/replicas
          TEMPLATE_NAME=my_template
          INDEX_PATTERN="logstash-*"
          SHARD_COUNT=8
          REPLICA_COUNT=1
          ES_URL=http://localhost:9200
          while [[ "$(curl -s -o /dev/null -w '%{http_code}\n' $ES_URL)" != "200" ]]; do sleep 1; done
          curl -XPUT "$ES_URL/_template/$TEMPLATE_NAME" -H 'Content-Type: application/json' -d'{"index_patterns":['\""$INDEX_PATTERN"\"'],"settings":{"number_of_shards":'$SHARD_COUNT',"number_of_replicas":'$REPLICA_COUNT'}}'
```

## Notes

### Rolling restart procedure
1. Stop indexing new data if possible
2. Disable shard allocation - to avoid the new shard allocation for the cluster to avoid shard rebalance. (cluster.routing.allocation.enable: none)
3. Shutdown one node
4. Perform the maintenance of the node, restart and confirm it joins the cluster.
5. Re-enable shard allocation  (cluster.routing.allocation.enable: all)
6. Wait for the cluster to return to green status
7. Repeat steps 2-6 for all other nodes
Resume indexing new data




[#63]: https://github.com/elastic/helm-charts/issues/63
[7.9]: https://github.com/elastic/helm-charts/blob/7.9/elasticsearch/README.md
[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/master/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/master/CHANGELOG.md
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md
[alternate scheduler]: https://kubernetes.io/docs/tasks/administer-cluster/configure-multiple-schedulers/#specify-schedulers-for-pods
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[anti-affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[cluster.name]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/cluster.name.html
[clustering and node discovery]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/README.md#clustering-and-node-discovery
[config example]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/config/values.yaml
[curator]: https://www.elastic.co/guide/en/elasticsearch/client/curator/5.8/snapshot.html
[custom docker image]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/docker.html#_c_customized_image
[deploys statefulsets serially]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#pod-management-policies
[discovery.zen.minimum_master_nodes]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/discovery-settings.html#minimum_master_nodes
[docker for mac]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/docker-for-mac
[elasticsearch cluster health status params]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/cluster-health.html#request-params
[elasticsearch docker image]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/docker.html
[elasticsearch oss docker image]: https://www.docker.elastic.co/r/elasticsearch/elasticsearch-oss
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[environment from variables]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
[examples]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/
[examples/multi]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/multi
[examples/oss]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/oss
[examples/security]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/security
[gke]: https://cloud.google.com/kubernetes-engine
[helm]: https://helm.sh
[helm 3 (beta)]: https://github.com/elastic/helm-charts/tree/master/README.md#helm-3-beta
[helm/charts stable]: https://github.com/helm/charts/tree/master/stable/elasticsearch/
[how to install plugins guide]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/README.md#how-to-install-plugins
[how to use the keystore]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/README.md#how-to-use-the-keystore
[http.port]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/modules-http.html#_settings
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/
[java options]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/jvm-options.html
[jvm heap size]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/heap-size.html
[kind]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/kubernetes-kind
[kubernetes secrets]: https://kubernetes.io/docs/concepts/configuration/secret/
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[lifecycle hooks]: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/
[loadBalancer annotations]: https://kubernetes.io/docs/concepts/services-networking/service/#ssl-support-on-aws
[loadBalancer externalTrafficPolicy]: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip
[loadBalancer]: https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer
[maxUnavailable]: https://kubernetes.io/docs/tasks/run-application/configure-pdb/#specifying-a-poddisruptionbudget
[migration guide]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/migration/README.md
[minikube]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/minikube
[microk8s]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/microk8s
[multi]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/multi/
[network.host elasticsearch setting]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/network.host.html
[node affinity settings]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#node-affinity-beta-feature
[node-certificates]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/configuring-tls.html#node-certificates
[nodePort]: https://kubernetes.io/docs/concepts/services-networking/service/#nodeport
[nodes types]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/modules-node.html
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[openshift]: https://github.com/elastic/helm-charts/tree/7.9/elasticsearch/examples/openshift
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[roles]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/modules-node.html
[secret]: https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets
[securityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
[service types]: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
[snapshot lifecycle management]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/snapshot-lifecycle-management.html
[snapshot plugin]: https://www.elastic.co/guide/en/elasticsearch/plugins/7.9/repository.html
[snapshot repository]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/modules-snapshots.html
[supported configurations]: https://github.com/elastic/helm-charts/tree/7.9/README.md#supported-configurations
[sysctl vm.max_map_count]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/vm-max-map-count.html#vm-max-map-count
[terminationGracePeriod]: https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[transport port configuration]: https://www.elastic.co/guide/en/elasticsearch/reference/7.9/modules-transport.html#_transport_settings
[updateStrategy]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
[values.yaml]: https://ssd-git.juniper.net/atom/atom/-/blob/master/third_party/helm/charts/elasticsearch/values.yaml
[volumeClaimTemplate for statefulsets]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-storage