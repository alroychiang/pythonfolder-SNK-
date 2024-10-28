#include "tensorflow/core/framework/tensor.h"
#include "tensorflow/core/framework/tensor_types.h"
#include "tensorflow/core/platform/logging.h"
#include "tensorflow/cc/ops/standard_ops.h"
#include "tensorflow/cc/client/client_session.h"
#include <algorithm>

USTRUCT(BlueprintType)
struct NEURALNETWORKS_API FNNTensor
{
    GENERATED_BODY()
public:
    // Constructor and other member functions omitted for brevity...

    bool IsAllOnes() const;
    bool IsAllZeros() const;

    tensorflow::Tensor tensor;
};

bool FNNTensor::IsAllOnes() const {
    auto flat_tensor = tensor.flat<float>();
    return std::all_of(flat_tensor.data(), flat_tensor.data() + flat_tensor.size(), [](float val) { return val == 1.0f; });
}

bool FNNTensor::IsAllZeros() const {
    auto flat_tensor = tensor.flat<float>();
    return std::all_of(flat_tensor.data(), flat_tensor.data() + flat_tensor.size(), [](float val) { return val == 0.0f; });
}

bool IsTensorAllOnesOrZeros(const FNNTensor& tensor) {
    return tensor.IsAllOnes() || tensor.IsAllZeros();
}

// Example usage
int main() {
    // Assuming you have a way to initialize an FNNTensor
    FNNTensor myTensor;

    // Initialize tensor with all ones or zeros
    // Example: myTensor.tensor = tensorflow::Tensor(tensorflow::DT_FLOAT, tensorflow::TensorShape({1, 88, 1}));
    //          myTensor.tensor.flat<float>().setConstant(1.0f); // or 0.0f for zeros

    bool result = IsTensorAllOnesOrZeros(myTensor);

    std::cout << "Is tensor all ones or all zeros? " << (result ? "Yes" : "No") << std::endl;

    return 0;
}
