version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "imagedefinitions.json"
        LoadBalancerInfo:
          ContainerName: "httpd-container"
          ContainerPort: 80
