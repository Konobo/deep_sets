class Rho(nn.Module):
    def __init__(self, input_size, output_size = 1):
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.fc1 = nn.Linear(self.input_size, 10)
        self.fc2 = nn.Linear(10, self.output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu()
        x = self.fc2(x)
        return x